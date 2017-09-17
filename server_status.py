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

check_service('nginx', {'name': 'NGINX', 'msg': 'Status of nginx'})
check_service('smbd', {'name': 'SAMBA', 'msg': 'Status of Samba server'})
check_service('transmission-daemon', {'name': 'TRANSMISSION', 'msg': 'Status of transmission-daemon'})

aegon_status = False
try:
	r = requests.get("http://192.168.0.87")
	if (r.status_code is 200):
		aegon_status = True
except Exception, err:
	aegon_status = False


log('AEGON', 'NetGear NAS @192.168.0.87', aegon_status)
row_log()

# Check JBlog access
class JBlog(object):
	def local(self):
		curl_local = requests.get('http://localhost:4000')
		local_result = False
		if (curl_local.status_code is 200):
			local_result = True
		log('JBlog', 'Status via Localhost on port 4000', local_result)
		
	def external(self):
		curl_extern = requests.get('http://46.7.248.23:80/jblog')
		extern_result = False
		if (curl_extern.status_code is 200):
			extern_result = True
		log('JBlog', 'Status via External IP on port 80', extern_result)

	def domain(self):	
		curl_domain = requests.get('http://www.Theseus.tk/jblog')
		domain_result = False
		if (curl_domain.status_code is 200):
			domain_result = True
		log('JBlog', 'Status via Domain name Theseus.tk/JBlog', domain_result)

jblog_check = JBlog()

jblog_check.local()
jblog_check.external()
jblog_check.domain()
end_log()

# Navigate to The correct directory
theseus_jblog_dir = '/home/barry/reverse_proxy/jblog'
os.chdir(theseus_jblog_dir)

# Check Git Status
print ('')
print('-- Git Status --')
subprocess.check_output("git fetch", shell=True)
status = subprocess.check_output("git status", shell=True)
git_msg = 'JBlog is '+ colored('behind', 'red') +' by '
if ("up-to-date" in status):
	git_msg = 'JBlog is branch origin/master ' + colored('up-to-date', 'green')
	print (git_msg)
else:
	start = status.find('by', 0, len(status))
	end = status.find(',', 0, len(status))
	behind_msg = status[start: end]
	print(git_msg + behind_msg)
	

	
	



