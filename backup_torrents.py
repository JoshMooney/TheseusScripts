import shutil
import os
import platform
import subprocess


def already_exist(_dir):
    if os.path.isdir(_dir) or os.path.isfile(_dir):
        return True
    return False

dirs = {
    "src": {"Windows": "F:/", "Linux": "/mnt/ShortTerm/torrents"},
    "dst": {"Windows": "F:/", "Linux": "/mnt/Aegon/Videos"}
}
finished = []
ver = platform.system()
ignore_dirs = ["_incomplete", "In_Progress", "$RECYCLE.BIN"]

files = [d for d in os.listdir(dirs['src'][ver])]
files = filter(lambda x: x not in ignore_dirs, files)
stats = {"pass": 0, "fail": 0, "skipped": 0}
file_count = 0

copy_complete_file = open('copy_complete.dat', 'w+')

for f in files:
    file_count += 1
    if os.path.isdir(dirs['dst'][ver]):
        src = os.path.join(dirs['src'][ver], f)
        dst = os.path.join(dirs['dst'][ver], f)

        print("Copying {} file {} of {}".format(f, file_count, len(files)))
        if already_exist(dst):
            print("The file {} already exists in the directory {}".format(f, dst))
            stats['skipped'] += 1
            continue
        try:
            if os.path.isdir(src):
                shutil.copytree(src, dst, False, None)
            else:
                shutil.copyfile(src, dst)
            print("Copied {} to {}".format(f, dirs['dst'][ver]))
            copy_complete_file.write(f)
            stats['pass'] += 1
        except OSError as error:
            print("Error copying with shutil, attempting terminal")
            try:
                subprocess.call(['cp', '-r', src, dst])
                print("Copied {} to {} using terminal".format(f, dirs['dst'][ver]))
                copy_complete_file.write(f)
                stats['pass'] += 1
            except Exception as error:
                print("Error copying with terminal, giving up")
                stats['fail'] += 1
        print("")
    else:
        print("Destination directory {} was not accessible".format(dirs['dst'][ver]))
        stats['skipped'] += 1
    print("")

print("** {} files copied, {} files failed and {} files skipped **.".format(stats['pass'], stats['fail'], stats['skipped']))
copy_complete_file.write("stats=successful:{},failed:{},skipped:{}". format(stats['pass'], stats['fsil'], stats['skipped']))
