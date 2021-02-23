import subprocess
import os

def _mount_aegon():
    print('Mounting Aegon')
    try:
        status = subprocess.check_output("sudo mount -t cifs //192.168.5.66/media /mnt/Aegon -o username=admin,password=itcarlow,vers=1.0 && sudo chown 777 /mnt/Aegon;", shell=True)    
	print ("Mounted @ /mnt/Aegon/")
    except Exception, e:
        print ('Error mounting Aegon')
    print('')
