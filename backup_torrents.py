import shutil
import os
import platform
import subprocess


def already_exist(_dir):
    if os.path.isdir(_dir) or os.path.isfile(_dir):
        return True
    return False


class BackupTorrents(object):
    def __init__(self):
        self.dirs = {
            "src": {"Windows": "F:/test_dir", "Linux": "/mnt/ShortTerm/torrents"},
            "dst": {"Windows": "F:/", "Linux": "/mnt/Aegon/Videos"}
        }
        self.finished = []
        self.ver = platform.system()
        self.ignore_dirs = ["_incomplete", "In_Progress", "$RECYCLE.BIN", "_whitelist"]
        self.stats = {"pass": 0, "fail": 0, "skipped": 0, "deleted": 0}
        self.files = self.get_files()

    def get_files(self):
        files = [d for d in os.listdir(self.dirs['src'][self.ver])]
        return filter(lambda x: x not in self.ignore_dirs, files)

    def delete_file(self, src):
        try:
            if already_exist(src):
                if os.path.isdir(src):
                    shutil.rmtree(src)
                else:
                    os.remove(src)
                self.stat_log("deleted")
                return True
            print("    ?? File no longer exists in source directory ??")
            return False
        except Exception as error:
            print("    There was an error deleting file")
            return False

    def copy_file(self, f, src, dst):
        try:
            if os.path.isdir(src):
                shutil.copytree(src, dst, False, None)
            else:
                shutil.copyfile(src, dst)
            self.stat_log('pass')
            return True
        except Exception as error:
            print("    Error copying file")
            self.stat_log('fail')
            return False

    def stat_log(self, type):
        self.stats[type] += 1

    def run_backup(self):
        file_count = 0
        print("** Starting Torrent Backup **")
        for f in self.files:
            file_count += 1
            if os.path.isdir(self.dirs['dst'][self.ver]):
                src = os.path.join(self.dirs['src'][self.ver], f)
                dst = os.path.join(self.dirs['dst'][self.ver], f)

                if already_exist(dst):
                    print("    The file {} already exists in the directory {} skipping".format(f, dst))
                    self.stat_log('skipped')
                    result = True
                else:
                    print("    Copying {} file {} of {}".format(f, file_count, len(self.files)))
                    result = self.copy_file(f, src, dst)
                    print("    Successfully copied {} to {} and was marked".format(f, self.dirs['dst'][self.ver]))

                if result:
                    print("    Deleteing {}".format(f))
                    self.delete_file(src)
                    print("    Successfully deleted {}".format(f))
                else:
                    print("    File did not copy and was not deleted")
            else:
                print("    Destination directory {} was not accessible".format(self.dirs['dst'][self.ver]))
                self.stat_log('skipped')
        print("Processed {} files: \n    - {} files copied,\n    - {} files failed,\n    - {} files skipped,\n    - {} deleted files".format(len(self.files), self.stats['pass'], self.stats['fail'], self.stats['skipped'], self.stats['deleted']))
        print("** Finished Torrent Backup **")


if __name__ == "__main__":
    backup = BackupTorrents()
    backup.run_backup()
