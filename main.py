import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "sender_email"
EMAIL_SENDER_NAME = "sender_name"
EMAIL_PASSWORD = "sender_app_password_"
EMAIL_RECIPIENT = "recipient_mail"


with open("email_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Create Email Message
message = MIMEMultipart()
message["From"] = f"{EMAIL_SENDER_NAME} <{EMAIL_SENDER}>"
message["To"] = EMAIL_RECIPIENT
message["Subject"] = "Test Email - Affirm Template"

# Attach HTML Content
message.attach(MIMEText(html_content, "html"))

# Send Email
try:
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)  # Secure Connection
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, message.as_string())

    print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Error sending email: {e}")