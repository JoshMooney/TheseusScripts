import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
fromaddr = "jmooney@digisoft.tv"
toaddr = "joshmoo2012@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "PythonSent"
 
body = "Sent from python"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "asgarthp90")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print('Finished')