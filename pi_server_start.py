import subprocess
import os
from _mount_aegon import _mount_aegon


def execute():
    print('-- Running Piesues start-up script --')

    # Run functions from here
    _run_nginx()
    _run_jblog()
    _run_api()
    
    _mount_aegon()
    _run_vncserver()
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
        print('Changing permissions on Tranmission Mounted Drive')
        status = subprocess.check_output("sudo chmod 777 -R /mnt/ShortTerm/", shell=True)
    except Exception, e:
        print ('Error starting Transmission-daemon: ', e)
    print('')

# Start Nginx
def _run_nginx():
    print('Starting Nginx')
    try:
        status = subprocess.check_output("sudo service nginx start", shell=True)
    except Exception, e:
        print ('Error starting Nginx: ', e)
    print('')

# Starting JBlog
def _run_jblog():
    try:
        print('Configuring JBlog')
        theseus_jblog_dir = '/home/pi/Project/JBlog'
        os.chdir(theseus_jblog_dir)
        print('Starting JBlog')
        status = subprocess.check_output("screen -d -m bundle exec jekyll serve", shell=True) 
    except Exception, e:
        print ('Error starting JBlog: ', e)
    print('')
    
# start api
def _run_api():
    try:
        print('Configuring API')
        theseus_api_dir = '/home/pi/Project/Theseus-API'
        os.chdir(theseus_api_dir)
        print('Starting Theseus-API')
        status = subprocess.check_output("screen -d -m python rest_api.py", shell=True) 
    except Exception, e:
        print ('Error starting API: ', e)
    print('')

def _run_minidlna():
    print('Starting miniDLNA')
    try:
        status = subprocess.check_output("sudo service minidlna start", shell=True)
    except Exception, e:
        print ('Error starting miniDLNA: ', e)
    print('')
    
#todo: start film-calender-ui

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

def _run_vncserver():
    try:
        print('Starting VNC Server')
        status = subprocess.check_output("vncserver", shell=True) 
    except Exception, e:
        print('Error running VNC Server: ')
    print('Finish VNC Server start')
    print('')

execute()

