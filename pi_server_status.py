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

check_service('nginx', {'name': 'NGINX', 'msg': 'Status of nginx'})
check_service('smbd', {'name': 'SAMBA', 'msg': 'Status of Samba server'})
check_service('transmission-daemon', {'name': 'TRANSMISSION', 'msg': 'Status of transmission-daemon'})
check_service('minidlna', {'name': 'MINIDLNA', 'msg': 'Status of miniDLNA server'})

def _check_teamviewer():
    log_msg = {'name': 'TeamViewer', 'msg': 'Status of TeamViewer Host'}
    status = subprocess.check_output("ps aux | grep teamviewer", shell=True)
    is_running = False
    if('/opt/teamviewer/tv_bin/TeamViewer'in status):
        is_running = True
    log(log_msg['name'], log_msg['msg'], is_running)
    row_log()
        
_check_teamviewer()

def _check_vnc_server():
    log_msg = {'name': 'VNC Server', 'msg': 'Status of VNC Server'}
    is_running = False
    try:
        status = subprocess.check_output("ps -e | grep vnc", shell=True)
        if('Xtightvnc'in status):
            is_running = True
        log(log_msg['name'], log_msg['msg'], is_running)
    except Exception as err:
        log(log_msg['name'], log_msg['msg'], is_running)
    row_log()
        
_check_vnc_server()

def _check_mounted_drives():
    drives = [{"name": "ShortTerm", "path": "/media/pi/ShortTerm"},
              {"name": "Aegon",     "path": "/mnt/Aegon"}]
    
    for d in drives:
        is_mounted = False
        if os.path.ismount(d['path']):
            is_mounted = True
        log(d['name'], d['name'] + ' is mounted @' + d['path'], is_mounted)
    row_log()
            
_check_mounted_drives() 

def _check_aegon_status():
	aegon_status = False
	try:
		r = requests.get("http://192.168.0.87")
		if (r.status_code is 200):
			aegon_status = True
	except Exception, err:
		aegon_status = False
	log('AEGON', 'NetGear NAS @192.168.0.87', aegon_status)


_check_aegon_status()

# Check JBlog access
class JBlog(object):
	def check_all(self):
		self.local()
		self.external()
		self.domain()

	def local(self):
		local_result = False
		try:
			curl_local = requests.get('http://localhost:4000')
			if (curl_local.status_code is 200):
				local_result = True
		except Exception, err:
			local_result = False
		log('JBlog', 'Status via Localhost on port 4000', local_result)
		
	def external(self):
		extern_result = False
		try:
			curl_extern = requests.get('http://'+ _external_ip +':80/jblog')
			if (curl_extern.status_code is 200):
				extern_result = True
		except Exception, err:
			extern_result = False
		log('JBlog', 'Status via External IP on port 80', extern_result)

	def domain(self):	
		domain_result = False
		try:
			curl_domain = requests.get('http://www.Theseus.tk/jblog')
			if (curl_domain.status_code is 200):
				domain_result = True
		except Exception, err:
			domain_result = False
		log('JBlog', 'Status via Domain name Theseus.tk/JBlog', domain_result)

	def git_status(self):
		print "Checking Git Status of JBlog"
		theseus_jblog_dir = '/home/pi/Project/JBlog'
		os.chdir(theseus_jblog_dir)
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

row_log()
jblog_check = JBlog()
jblog_check.check_all()

# Check API access
class API(object):
	def check_all(self):
		self.local()
		self.external()
		self.domain()

	def local(self):
		local_result = False
		try:
			curl_local = requests.get('http://localhost:5000')
			if (curl_local.status_code is 200):
				local_result = True
		except Exception, err:
			local_result = False
		log('API', 'Status via Localhost on port 5000', local_result)
		
	def external(self):
		extern_result = False
		try:
			curl_extern = requests.get('http://'+ _external_ip +':80/rest')
			if (curl_extern.status_code is 200):
				extern_result = True
		except Exception, err:
			extern_result = False
		log('API', 'Status via External IP on port 80', extern_result)

	def domain(self):	
		domain_result = False
		try:
			curl_domain = requests.get('http://www.Theseus.tk/rest')
			if (curl_domain.status_code is 200):
				domain_result = True
		except Exception, err:
			domain_result = False
		log('API', 'Status via Domain name Theseus.tk/rest', domain_result)

row_log()
api_check = API()
api_check.check_all()

# Check Film_Calendar access
class Film_Calendar(object):
	def check_all(self):
		self.local()
		self.external()
		self.domain()

	def local(self):
		local_result = False
		try:
			curl_local = requests.get('http://localhost:80/film-ui')
			if (curl_local.status_code is 200):
				local_result = True
		except Exception, err:
			local_result = False
		log('Film', 'Status via Localhost on port 80', local_result)
		
	def external(self):
		extern_result = False
		try:
			curl_extern = requests.get('http://'+ _external_ip +':80/film-ui')
			if (curl_extern.status_code is 200):
				extern_result = True
		except Exception, err:
			extern_result = False
		log('Film', 'Status via External IP on port 80', extern_result)

	def domain(self):	
		domain_result = False
		try:
			curl_domain = requests.get('http://www.Theseus.tk/film-ui')
			if (curl_domain.status_code is 200):
				domain_result = True
		except Exception, err:
			domain_result = False
		log('Film', 'Status via Domain name Theseus.tk/film-ui', domain_result)

row_log()
calendar_check = Film_Calendar()
calendar_check.check_all()

class Resume(object):
    def check_all(self):
        self.local()
        self.external()

    def local(self):
        local_result = False
        try:
            curl_local = requests.get('http://localhost:80/resume')
            if (curl_local.status_code is 200):
                local_result = True
        except Exception as err:
            local_result = False
        log('Resume', 'Status of /resume endpoint using a Local IP', local_result)

    def external(self):
        extern_result = False
        try:
            curl_extern = requests.get('http://' + _external_ip + ':80/resume')
            if (curl_extern.status_code is 200):
                extern_result = True
        except Exception as err:
            extern_result = False
        log('Resume', 'Status of /resume endpoint using a External IP', extern_result)

    def git_status(self):
        print
        "Checking Git Status of JBlog"
        theseus_jblog_dir = '/home/pi/Project/PieseusResume'
        os.chdir(theseus_jblog_dir)
        subprocess.check_output("git fetch", shell=True)
        status = subprocess.check_output("git status", shell=True)
        git_msg = 'Resume is ' + colored('behind', 'red') + ' by '
        if ("up-to-date" in status):
            git_msg = 'Resume is branch origin/master ' + colored('up-to-date', 'green')
            print(git_msg)
        else:
            start = status.find('by', 0, len(status))
            end = status.find(',', 0, len(status))
            behind_msg = status[start: end]
            print(git_msg + behind_msg)

row_log()
resume_check = Resume()
resume_check.check_all()
end_log()

# Navigate to The correct directory
theseus_jblog_dir = '/home/pi/Project/JBlog'
os.chdir(theseus_jblog_dir)

# Check Git Status
print ('')
print('-- Git Status --')

jblog_check.git_status()
resume_check.git_status()
	
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
     
   
    