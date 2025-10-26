import yagmail


def Mailer(app_psw,gmail,datas):
    smtp = yagmail.SMTP(user=gmail, password= app_psw)
    smtp.send(
        to=gmail,
        subject= "Followers",
        contents= datas
    )
    smtp.close()

