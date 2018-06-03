"""

    requirements.txt:
        - shutil
"""

import shutil


scripts = [
    {"name": "pi_server_startup.py", "des": "/home/pi/.scripts.bin", "src": "/home/pi/Project/TheseusScripts"},
    {"name": "pi_server_status.py", "des": "/home/pi/.scripts.bin", "src": "/home/pi/Project/TheseusScripts"}
]

print("** Updating Pieseus Scripts **")

for script in scripts:
    try:
        print("    Copying {}".format(script['name']))
        src = "{}/{}".format(script['src'], script['name'])
        des = "{}/{}".format(script['des'], script['name'])
        shutil.copyfile(src, des)
	print("    Finsihed copying {}".format(script['name']))
	print("")
    except Exception as error:
	print("")
        print("******************************************")
	print("")
	print("    Failed to copy %s" % script['name'])
	print("    " + str(error))
	print("")
	print("******************************************")
	print("")



print("** Finished Updating Scripts **")
