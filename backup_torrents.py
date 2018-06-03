import shutil
import os

src = "/home/pi/Project/TheseusScripts"
des_dir = "Aegon somewhere"

finished = []

files = [x[0] for x in os.walk(src)]

for f in files:
    if "_incomplete" not in f and f is not src:
        print f

    # Verify Aegon
    # try copy to Aegon if connected

#print progress

