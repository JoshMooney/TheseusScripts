"""

    requirements.txt:
        - shutil
"""

import shutil


scripts = [
    {"name": "test_file.txt", "des": "/home/pi/.scripts.bin", "src": "/home/pi/Project/TheseusScripts"}
    #{"name": "pi_server_startup.py", "des": "/home/pi/.scripts.bin", "src": "/home/pi/Project/TheseusScripts"},
    #{"name": "pi_server_status.py", "des": "/home/pi/.scripts.bin", "src": "/home/pi/Project/TheseusScripts"}
]

print("** Updating Pieseus Scripts **")

for script in scripts:
    try:
        print("Copying %s" % script['name'])
        src = "&s/%s" % script['src'], script['name']
        des = "&s/%s" % script['des'], script['name']
        shutil.copyfile(src, des)
    except Exception as error:
        print("Failed to copy %s" % script['name'])



print("** Finished Updating Scripts **")