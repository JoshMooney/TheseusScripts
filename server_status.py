import subprocess
import requests
import os
from termcolor import colored

template = "| {0:18} | {1:52} | {2:18} |"
print template.format("SERVICE", "MESSAGE", "STATUS")

def log(ser, msg, stat):
	stat_col = 'red'
	stat_msg = 'down'
	if stat is True:
		stat_col = 'green'
		stat_msg = 'active'
	print template.format(ser, msg, colored(stat_msg, stat_col))

# Check Nginx staus
status = subprocess.check_output("service nginx status", shell=True)
nginx_status = False
if ("Active: active (running)" in status):
	nginx_status = True
log('NGINX', 'Status of nginx', nginx_status)

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

# Navigate to The correct directory
theseus_jblog_dir = '/home/barry/reverse_proxy/jblog'
os.chdir(theseus_jblog_dir)

# Check Git Status
subprocess.check_output("git fetch", shell=True)
status = subprocess.check_output("git status", shell=True)
git_msg = 'JBlog is behing by '
if ("up-to-date" in status):
	git_msg = 'JBlog is up to date'
	print (git_msg)
else:
	start = status.index('by', 100)
	end = status.find(',', 100)
	behind_msg = status[start: end]
	print(git_msg + behind_msg)
	

	
	



