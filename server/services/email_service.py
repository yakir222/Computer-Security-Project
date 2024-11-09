import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email, newPassword) -> bool:
    print(f"Sending email to {email}")
    sender_email = "computersecnnyl@gmail.com"
    password = "eepumybnbgmonycb"
    receiver_email = email

    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Password Reset mail"
    body = f"Hi! you requested a password change, this is the new password - {newPassword}."
    print(f"mail body is {body}")
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print("Problem sending email :(")
        print(e)
        return False
    print("Email sent successfully!")
    return True

if __name__=="__main__":
    EmailService.send_email("ginjos1@gmail.com","c59d30150efdb5fa60cfbc81c9bc2cd7c4540a4d")
