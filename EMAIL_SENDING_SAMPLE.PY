import os
import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = os.environ.get('MY_EMAIL')
my_email_pass = os.environ.get('MY_EMAIL_PASS')

def notify_user(subject, body):
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(my_email, my_email_pass)
		msg = MIMEMultipart('alternative')
		msg['Subject'] = subject
		html = body
		part2 = MIMEText(html, 'html')
		msg.attach(part2)

		#subject = 'Hi this is yuvi'
		#body = 'Hi There!! \n Yuvi here'
		# msg = f'Subject: {subject} \n\n{body}'
		# print(my_email,msg)


		smtp.sendmail(my_email, 'yuvarajthiyagarajan28@gmail.com', msg.as_string())
		smtp.close()

# try:
# 	r = requests.get('http://127.0.0.1:8000', timeout= 5)
# 	if r.status_code != 200:
# 		print('test')
# 		notify_user()
# except Exception as e:
# 	print('error test')
# 	notify_user()