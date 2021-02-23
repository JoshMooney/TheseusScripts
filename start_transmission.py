import subprocess

print('Starting Transmission-daemon')
try:
    status = subprocess.check_output("sudo service transmission-daemon start", shell=True)
    # Only nessasary for the RAID setup on Pieseus
    #print('Changing permissions on Tranmission Mounted Drive')
    #status = subprocess.check_output("sudo chmod 777 -R /mnt/ShortTerm/", shell=True)
except Exception, e:
    print ('Error starting Transmission-daemon: ', e)
print('')
