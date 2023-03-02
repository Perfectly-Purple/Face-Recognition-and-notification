import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_email(strTo= 'surabhi.annigeri@gmail.com',image1='test.png'):
    strFrom = 'cambotnotif@gmail.com'
    msgRoot = MIMEMultipart()
    msgRoot['Subject'] = 'New Visitor'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgText = MIMEText('<b>You have a new visitor(s).</b><br><br><br><img src="cid:img"><br>', 'html')
    msgRoot.attach(msgText)
    fp = open(image1, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<img>')
    msgRoot.attach(msgImage)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('cambotnotif@gmail.com', 'feeincifwxgajbqm')
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        smtp.quit()