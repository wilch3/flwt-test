"""Email configuration and sender."""
import smtplib, ssl
import json

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_config():
    """Reads authentication data stored in 'email.json' file."""
    with open("utils/json/email.json", "r") as file:
        data = json.load(file)

    return data["email"]


def send_email(recipient, subject, attachment, body):
    """Configures email and sends it out

    :param recipient: Email of a person that will receive the email as string
    :param subject: Subject of the email
    :param attachment: Path to file attached to the email
    :param body: Plaintext body
    """
    auth = read_config()  # read authentication data from a file

    sender = auth["login"]
    password = auth["password"]

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    # Attach readable - plain - text
    message.attach(MIMEText(body, "plain"))

    file = attachment
    with open(file, "rb") as pdf:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(pdf.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename={file}",
    )

    message.attach(part)
    text = message.as_string()

    # Log in to server using secure ssl context
    cont = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=cont) as server:  # Gmail only, change smtp server if necessary
        server.login(sender, password)
        server.sendmail(sender, recipient, text)  # send email
