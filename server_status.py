import subprocess
import requests
import os
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

start_log()
template = "| {0:18} | {1:52} | {2:18} |"
print template.format("SERVICE", "MESSAGE", "STATUS")
row_log()

# Check Nginx staus
status = subprocess.check_output("service nginx status", shell=True)
nginx_status = False
if ("Active: active (running)" in status):
	nginx_status = True
log('NGINX', 'Status of nginx', nginx_status)
row_log()

# Transmission status
status = subprocess.check_output("service transmission-daemon status", shell=True)
trans_status = False
if ("Active: active (running)" in status):
	trans_status = True
log('TRANSMISSION', 'Status of transmission-daemon', trans_status)
row_log()

# Samba status
status = subprocess.check_output("service smbd status", shell=True)
samba_status = False
if ("Active: active (running)" in status):
	samba_status = True
log('SAMBA', 'Status of Samba server', samba_status)
row_log()

# Check JBlog access
curl_local = requests.get('http://localhost:4000')
local_result = False
if (curl_local.status_code is 200):
	local_result = True
log('JBlog', 'Status via Localhost on port 4000', local_result)
	
curl_extern = requests.get('http://46.7.248.23:80/jblog')
extern_result = False
if (curl_extern.status_code is 200):
	extern_result = True
log('JBlog', 'Status via External IP on port 80', extern_result)
	
curl_domain = requests.get('http://www.Theseus.tk/jblog')
domain_result = False
if (curl_extern.status_code is 200):
	domain_result = True
log('JBlog', 'Status via Domain name Theseus.tk/JBlog', domain_result)

end_log()

if domain_result and extern_result and local_result:
	print ('')
	print('-- JBlog is full functional! --')

# Navigate to The correct directory
theseus_jblog_dir = '/home/barry/reverse_proxy/jblog'
os.chdir(theseus_jblog_dir)

# Check Git Status
print ('')
print('-- JBlog Git Status --')
subprocess.check_output("git fetch", shell=True)
status = subprocess.check_output("git status", shell=True)
git_msg = 'JBlog is '+ colored('behind', 'red') +' by '
if ("up-to-date" in status):
	git_msg = 'JBlog is ' + colored('up-to-date', 'green')
	print (git_msg)
else:
	start = status.find('by', 0, len(status))
	end = status.find(',', 0, len(status))
	behind_msg = status[start: end]
	print(git_msg + behind_msg)
	

	
	



