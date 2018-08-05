#email send out
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587

sender_email = 'gmail'
receiver_email = 'to_mail'
content_email = '你好: \n這是從 Python 發送出來的 Email, 啾咪！'
# email='Ahua'
pw='password' #GMAIL 帳戶設定
msg = MIMEText(content_email.encode('utf-8'), _charset='utf-8')
msg['Subject'] = 'Hello 你好'
msg['From'] = "Ahua"
msg['To'] = receiver_email

conn = SMTP(host, port)
# conn = SMTP('smtp.gmail.com:587')
conn.ehlo()
conn.starttls()
try:
    conn.login(sender_email, pw)
    
    conn.sendmail(sender_email,receiver_email,msg.as_string())
    print("send ok")
except SMTPAuthenticationError:
    print("Could not login")
except SMTPException:
    print("an error occured")

conn.quit()



