import shutil
import os
import platform


dirs = {
    "src": {"Windows": "F:/", "Linux": "/mnt/ShortTerm/torrents"},
    "dst": {"Windows": "None", "Linux": "/mnt/Aegon/Videos/"}
}
finished = []
ver = platform.system()
ignore_dirs = ["_incomplete", "In_Progress", "$RECYCLE.BIN"]

files = [d for d in os.listdir(dirs['src'][ver])]
files = filter(lambda x: x not in ignore_dirs, files)

for f in files:
    if os.path.isdir(dirs['dst'][ver]):
        print f
        #shutil.copyfile(dirs['src'][ver], dirs['dst'][ver])
    else:
        print("Destination directory {} was not accessible".format(dirs['dst'][ver]))
    # try copy to Aegon if connected

#print progress

