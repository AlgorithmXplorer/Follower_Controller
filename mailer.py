import yagmail


def Mailer(app_psw,gmail,datas):
    smtp = yagmail.SMTP(user=gmail, password= app_psw)
    smtp.send(
        to=gmail,
        subject= "Followes",
        contents= datas
    )
    smtp.close()

