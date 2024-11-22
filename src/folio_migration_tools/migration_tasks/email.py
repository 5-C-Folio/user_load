import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


sender_email = "email@umass.edu"
receiver_email = "aneslin@umass.edu"
password = "your_password"
smtp_server = "smtp.example.com"
smtp_port = 587

def sendEmail (subject, body, attach):

    subject = subject
    body = body


    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject


    message.attach(MIMEText(body, "plain"))


    file_path = attach
    try:
        # Add the attachment
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode the attachment to base64
        encoders.encode_base64(part)

        # Add headers to the attachment
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_path.split('/')[-1]}"  # Extract filename from path
        )

        # Attach the file to the email
        message.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, password)  # Log in to the email account
            server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
            print("Email sent successfully with attachment!")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
