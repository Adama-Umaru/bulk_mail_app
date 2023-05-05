import smtplib
import ssl
from email.message import EmailMessage

# Prompt user for email details
sender_email = input("Enter your email address: ")
sender_password = input("Enter your email password: ")
recipient_emails = input("Enter the recipients email address: ")
email_subject = input("Enter the email subject: ")
email_body = input("Enter the email body: ")


# construct email message
email_msg = EmailMessage()

email_msg['Sbject'] = email_subject
email_msg['From'] = sender_email
email_msg['To'] = recipient_emails
email_msg.set_content(email_body)

context = ssl.create_default_context()

# Set up SMTP server
with smtplib.SMTP_SSL('smtp.gmail,com', 465, context= context) as smtp:
    smtp.login(sender_email,sender_password)
    smtp.sendmail(sender_email,recipient_emails, email_msg.as_string())

# Send email
if email_msg:
    print("Email sent successfully")
else:
    print("Email not sent successfully")

# Close SMTP server
smtp.quit()

