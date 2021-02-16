import subprocess
import os

def _mount_raid_cache():
    print('Mounting RAID Cache')
    try:
        status = subprocess.check_output("sudo mount /dev/md0 /RAID-cache", shell=True)    
    except Exception, e:
        print ('Error mounting RAID Cache')
    print('')
