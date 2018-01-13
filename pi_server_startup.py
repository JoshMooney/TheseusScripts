import subprocess
import os



def execute():
    print('-- Running Piesues start-up script --')

    # Run functions from here
    _run_nginx()
    _run_jblog()
    _run_api()

    _run_status()
    print('-- Startup Script Complete --')

# Start Nginx
def _run_nginx():
    print('Starting Nginx')
    try:
        status = subprocess.check_output("sudo service nginx start", shell=True)
    Exception e:
        print ('Error starting Nginx: ', e)

# Starting JBlog
def _run_jblog():
    try:
        print('Configuring JBlog')
        theseus_jblog_dir = '/home/pi/Projects/JBlog'
        os.chdir(theseus_jblog_dir)
        print('Starting JBlog')
        status = subprocess.check_output("screen -d -m bundle exec jekyll serve", shell=True) 
    Exception e:
        print ('Error starting JBlog: ', e)

# start api
def _run_api():
    try:
        print('Configuring API')
        theseus_api_dir = '/home/pi/Projects/Theseus-API'
        os.chdir(theseus_api_dir)
        print('Starting Theseus-API')
        status = subprocess.check_output("screen -d -m python rest_api.py", shell=True) 
    Exception e:
        print ('Error starting API: ', e)

#todo: start film-calender-ui

# Run Status script
def _run_status():
    try:
        print('Configuring Status')
        theseus_scripts_dir = '/home/pi/Projects/TheseusScripts'
        os.chdir(theseus_scripts_dir)
        print('Checking Status \n\n')
        status = subprocess.check_output("python server_status.py", shell=True) 
    Exception e:
        print ('Error running Status: ', e)

execute()