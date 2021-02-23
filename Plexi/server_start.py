import subprocess
import os
from _mount_aegon import _mount_aegon


def execute():
    print('-- Running Piesues start-up script --')
    
    _mount_aegon()
    _run_samba()
    _run_transmission()

    #_run_status()
    print('-- Startup Script Complete --')


# Start Samba
def _run_samba():
   print('Starting Samba')
   try:
       status = subprocess.check_output("sudo /etc/init.d/samba start", shell=True)
   except Exception, e:
       print ('Error starting Samba: ', e)
   print('')

# Start Transmission-daemon
def _run_transmission():
    print('Starting Transmission-daemon')
    try:
        status = subprocess.check_output("sudo service transmission-daemon start", shell=True)
    except Exception, e:
        print ('Error starting Transmission-daemon: ', e)
    print('')
    

# Run Status script
def _run_status():
    try:
        print('Configuring Status')
        theseus_scripts_dir = '/home/pi/Project/TheseusScripts'
        os.chdir(theseus_scripts_dir)
        print('Running Status script \n')
        status = subprocess.check_output("python pi_server_status.py", shell=True) 
    except Exception, e:
        print ('Error running Status script: ', e)
    print('')      

execute()

