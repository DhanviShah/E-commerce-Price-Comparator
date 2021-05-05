from smtplib import SMTP

def send_mail(sender,to):
  server = SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login('daamjano@gmail.com','Qwerty123%')
  subject = 'Alert! Prices have dropped!'
  body = '''Why wait! The prices have dropped, follow the link below and buy now.'''

  msg = f'subject: {subject} \n\n {body}'

  server.sendmail(sender,to,msg)
  print('Mail sent successfully!')
  server.quit()

to = ['srishtikalra65@gmail.com','dhanvi2301@gmail.com']
sender = 'daamjano@gmail.com'

send_mail(sender,to)
