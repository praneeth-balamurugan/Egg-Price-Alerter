import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = to

    user = "email.alert.praneeth10b@gmail.com"
    msg['from']=user
    password = "tibr iufk cphm zdqd"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    email_alert("HEYY", "HELLO WORLD", "praneeth.nkl@gmail.com")
