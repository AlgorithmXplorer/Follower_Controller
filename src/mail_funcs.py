import yagmail
import imaplib
import email
import re

# This function is used to send the follower data it receives as an email.
# To do this, it connects to the SMTP server with yagmail and sends the email.
def Mailer(app_psw,gmail,datas):
    smtp = yagmail.SMTP(user=gmail, password= app_psw)
    smtp.send(
        to=gmail,
        subject= "Followers",
        contents= datas
    )
    smtp.close()

# The purpose of this function is to read the verification code sent to your email when GitHub requires authentication.
# It performs the reading process using the imaplib module. You can access the module's documentation
# from the link below: https://docs.python.org/3/library/imaplib.html
def mail_reader(gmail,app_pasw) -> str:
    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    mail.login(gmail, app_pasw)
    mail.select("inbox")
    status, data = mail.search(None, 'FROM "noreply@github.com"')
    mail_ids = data[0].split() 
    last_mail_id = mail_ids[-1]       
    status, msg_data = mail.fetch(last_mail_id, '(RFC822)')
    msg = email.message_from_bytes(msg_data[0][1])
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode()
                return body            
    else:
        body = msg.get_payload(decode=True).decode()
    
    code = re.findall("[0-9]{6}",body)
    return code[0]
