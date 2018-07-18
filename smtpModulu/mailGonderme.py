import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


mesaj = MIMEMultipart()

mesaj["From"] = "kendi mailinizi"
mesaj["To"] = "göndereceğiniz kişinin mailini"
mesaj["Subject"] = "SMTP ile Mail Gönderme"

yazi = """

Merhaba Mustafa nasılsın?

Sana SMTP Modülü kullanarak mail gönderiyorum..

Ve Python alanında ilerlemeni tavsiye ediyorum..

"""

mesajGovdesi = MIMEText(yazi, "plain")

mesaj.attach(mesajGovdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()

    mail.login("Buraya mail adresinizi giriyorsunuz", "buraya kendi mailinizin şifresini giriyorsunuz....")
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail başarıyla gönderildi..")
    mail.close()

except:
    sys.stderr.write("Bir sorun var...")
    sys.stderr.flush()



