import multiprocessing
import time
import smtplib
from email.mime.text import MIMEText
_user = "1069923094@qq.com"
_pwd  = "ctacufjpmpafbcfd"
_to   = "aimee.tu@thegenuinelabs.com"

msg = MIMEText("hello,send by python...")
msg["Subject"] = "send email"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print ("Success!")
except smtplib.SMTPException,e:
    print("Falied,%s" % e)



print("hahhahah")


