import subprocess
import os

print('-- Running Startup Script --')

# Start Nginx
print('Starting nginx')
status = subprocess.check_output("sudo service nginx start", shell=True)

# Starting JBlog
theseus_jblog_dir = '/home/barry/reverse_proxy/jblog'
os.chdir(theseus_jblog_dir)
print('Starting JBlog')
status = subprocess.check_output("screen -d -m bundle exec jekyll serve", shell=True) 

# Run Status script
theseus_scripts_dir = '/home/barry/Scripts/TheseusScripts'
os.chdir(theseus_scripts_dir)
print('Checking Status \n\n')
status = subprocess.check_output("python server_status.py", shell=True) 

print('-- Startup Script Complete --')