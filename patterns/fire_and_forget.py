import asyncio
import smtplib
from email.message import EmailMessage

async def send_email(subject, body, to):
    # Create a new email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'me@example.com'
    msg['To'] = to
    msg.set_content(body)
    # Connect to the SMTP server and send the message
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        await smtp.starttls()
        await smtp.login('my_email@gmail.com', 'my_password')
        await smtp.send_message(msg)

# Fire-and-forget sending the email
asyncio.create_task(send_email('Test Email', 'This is a test email', 'you@example.com'))

# Continue with other work without waiting for the email to send
print('Email sent in the background')