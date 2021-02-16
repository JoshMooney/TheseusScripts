import subprocess
import os

def check_storage():
    try:
        status = subprocess.check_output("df -h /mnt/*", shell=True)
	return status
    except Exception, e:
        return 'Error checking storage status'

if __name__ == '__main__':
    print('Storage Capacity')
    print(check_storage())
