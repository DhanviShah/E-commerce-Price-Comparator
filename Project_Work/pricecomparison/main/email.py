from smtplib import SMTP

def send_mail(sender,to,data):
    server = SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('daamjano@gmail.com','Qwerty123%')
    subject = 'Alert! Prices have dropped!'
    body = f'Your product is: {data["p"]} \n\n Amazon link is: {data["a"]} \n Amazon price is: {data["pA"]} \n\n Flipkart link is: {data["f"]} \n Flipkart price is: {data["pF"]} \n\n Croma link is: {data["c"]} \n Croma price is: {data["pC"]}'

    msg = f'subject: {subject} \n\n {body}'
    sender=sender
    to = to
    server.sendmail(sender,to,msg)
    print(to)
    print('Mail sent successfully!')
    server.quit()
