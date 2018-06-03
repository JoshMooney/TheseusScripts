import shutil
import os
import platform


dirs = {
    "src": {"Windows": "F:/test_dir/", "Linux": "/mnt/ShortTerm/torrents"},
    "dst": {"Windows": "F:/", "Linux": "/mnt/Aegon/Videos"}
}
finished = []
ver = platform.system()
ignore_dirs = ["_incomplete", "In_Progress", "$RECYCLE.BIN"]

files = [d for d in os.listdir(dirs['src'][ver])]
files = filter(lambda x: x not in ignore_dirs, files)
stats = {"pass": 0, "fail": 0}

for f in files:
    if os.path.isdir(dirs['dst'][ver]):
        print f
        src = os.path.join(dirs['src'][ver], f)
        dst = os.path.join(dirs['dst'][ver], f)
        if os.path.isdir(src):
            shutil.copytree(src, dst, False, None)
        else:
            shutil.copyfile(src, dst)
        stats['pass'] += 1
        print("Copied {} to {}".format(f, dirs['dst'][ver]))
    else:
        print("Destination directory {} was not accessible".format(dirs['dst'][ver]))
        stats['fail'] += 1

print("** {} files copied, {} files failed **.".format(stats['pass'], stats['fail']))

