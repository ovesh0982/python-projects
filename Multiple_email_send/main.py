import smtplib 
from email.mime.text import MIMEText

sender_email = "basanaziz0982@gmail.com"
app_password = "09820982"  # Use app password if 2FA is enabled
recipient_email = "oveshaziz123@gmail.com"
subject = "Test Email"
body = "This is a test email."

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")

# ob =s.SMTP('smtp.gmail.com',587)
# ob.ehlo()
# ob.starttls()
# ob.login('basanaziz0982@gmail.com','09820982')
# subject = "Testing Python"
# body = "I Love Python"
# massage = "subject:{}\n\n{}".format(subject,body)
# listadd = ['basanaziz0982@gmail.com','oveshaziz123@gmail.com']
# ob.sendmail('oveshaziz123@gmail.com',listadd,massage)
# print("hellio")
# ob.quit()
