from argparse import ArgumentParser
from json import load
import sys
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

parser = ArgumentParser("quick-mail")
parser.add_argument("-f", "--file")
parser.add_argument("to")
parser.add_argument("message")
args = parser.parse_args()

file = args.file
if file:
    with open(file) as f:
        config = load(f)
else:
    config = load(sys.stdin)

with SMTP_SSL(config["host"], config.get("port", 465)) as smtp:
    username = config["username"]
    smtp.login(username, config["password"])
    message = MIMEMultipart()
    message["From"] = username
    to = message["To"] = args.to
    message.attach(MIMEText(args.message, "plain"))
    smtp.send_message(message, username, to)
