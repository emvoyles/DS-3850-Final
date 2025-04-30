import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, recipient_email):
    # Email credentials (you can load these from environment variables too)
    sender_email = "emvoyles42@tntech.edu"
    sender_password = "Classof22knowshowtoparty!"

    # SMTP server details (Gmail SMTP server)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body with the message
    msg.attach(MIMEText(body, 'plain'))

    # Set up the server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
