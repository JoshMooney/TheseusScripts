import shutil
import os
import platform
import subprocess
import re

def already_exist(_dir):
    if os.path.isdir(_dir) or os.path.isfile(_dir):
        return True
    return False

class BackupTorrents(object):
    def __init__(self):
        self.dirs = {
            "src": {"Windows": "F:/test_dir", "Linux": "/RAID-cache/torrents"},
            "dst": {"Windows": "F:/", "Linux": "/mnt/Aegon/Videos"}
        }
        self.finished = []
        self.ver = platform.system()
        self.ignore_dirs = ["_incomplete", "In_Progress", "$RECYCLE.BIN", "_whitelist"]
        self.stats = {"pass": 0, "fail": 0, "skipped": 0, "deleted": 0}
        self.files = self.get_files()

    def is_tv_show(self, _title):
        tv_show_reg_ex = "[sS][0-9]{1,2}[eE][0-9]{1,2}"
        return re.search(tv_show_reg_ex, _title)

    def is_movie(self, _title):
        movie_reg_ex = "[(\[][0-9]{4}[)\]]"
        return re.search(movie_reg_ex, _title)

    def get_destination_directory(self, _title):
        sub_path = ""
        
        if self.is_tv_show(_title):
            sub_path = "/TV"
        elif self.is_movie(_title):
            sub_path = "/Movies"
        
        if sub_path != "":
            return os.path.join(self.dirs['dst'][self.ver] + sub_path, _title)
        return os.path.join(self.dirs['dst'][self.ver], _title)

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
                dst = self.get_destination_directory(f)

                if already_exist(dst):
                    print("    The file {} already exists in the directory {} skipping".format(f, dst))
                    self.stat_log('skipped')
                    result = True
                else:
                    print("    Copying {} file {} of {}".format(f, file_count, len(self.files)))
                    result = self.copy_file(f, src, dst)
                    print("    {} {} to {}".format("Successfully copied" if result else "Failed to copy", f, dst))

                if result:
                    print("    Deleteing {}".format(f))
                    self.delete_file(src)
                    print("    Successfully deleted {}".format(f))
                else:
                    print("    File did not copy and was not deleted")
            else:
                print("    Destination directory {} was not accessible".format(self.dirs['dst'][self.ver]))
                self.stat_log('skipped')
        print("Processed {} files: \n    - {} files copied,\n    - {} files failed,\n    - {} files skipped,\n    - {} deleted files"
              .format(len(self.files), self.stats['pass'], self.stats['fail'], self.stats['skipped'], self.stats['deleted']))
        print("** Finished Torrent Backup **")


if __name__ == "__main__":
    backup = BackupTorrents()

    if os.geteuid() == 0:
        backup.run_backup()
    else:
        print("Script wont run, it was run with user privileges rather than sudo")
