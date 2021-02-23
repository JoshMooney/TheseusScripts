import subprocess
import requests
import os
import platform
from termcolor import colored

def start_log():
	print('|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|')
def row_log():
	print('|---------------------------------------------------------------------------------------|')
def end_log():
	print('|_______________________________________________________________________________________|')

def log(ser, msg, stat):
	stat_col = 'red'
	stat_msg = 'down'
	if stat is True:
		stat_col = 'green'
		stat_msg = 'active'
	print template.format(ser, msg, colored(stat_msg, stat_col))

_external_ip = "80.111.5.9"

start_log()
template = "| {0:18} | {1:52} | {2:18} |"
print template.format("SERVICE", "MESSAGE", "STATUS")
row_log()

def check_service(ser_name, ser_data):
	service_status = False
	try:
		status = subprocess.check_output("service "+ ser_name +" status", shell=True)
		if ("Active: active (running)" in status):
			service_status = True
	except Exception, err:
		service_status = False
	log(ser_data['name'], ser_data['msg'], service_status)
	row_log()

check_service('smbd', {'name': 'SAMBA', 'msg': 'Status of Samba server'})
check_service('transmission-daemon', {'name': 'TRANSMISSION', 'msg': 'Status of transmission-daemon'})


def _check_mounted_drives():
    drives = [{"name": "Aegon", "path": "/mnt/Aegon"}]
    
    for d in drives:
        is_mounted = False
        if os.path.ismount(d['path']):
            is_mounted = True
        log(d['name'], d['name'] + ' is mounted @ ' + d['path'], is_mounted)
    row_log()
            
_check_mounted_drives() 

def _check_aegon_status():
	aegon_status = False
	try:
		r = requests.get("http://192.168.5.66")
		if (r.status_code is 200):
			aegon_status = True
	except Exception, err:
		aegon_status = False
	log('AEGON', 'NetGear NAS @192.168.5.66', aegon_status)

_check_aegon_status()
	
# Get server uptime
print ('')
print('-- Server Uptime --')
try:
	status = subprocess.check_output("uptime", shell=True)
	start = status.find('up', 0, len(status))
	end = status.find(',', 0, len(status))
	up_time = status[start: end]
	comp_name = platform.node()
	print(comp_name+ " server has been " + up_time)
except Exception, err:
	print err
	print "Error getting uptime."
	 
print("")
     
   
    
