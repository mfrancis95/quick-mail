from argparse import ArgumentParser
from json import load
import sys
from smtplib import SMTP_SSL

parser = ArgumentParser("quick-mail")
parser.add_argument("to")
parser.add_argument("message")
args = parser.parse_args()

config = load(sys.stdin)

with SMTP_SSL(config["host"], config.get("port", 465)) as smtp:
    username = config["username"]
    smtp.login(username, config["password"])
    smtp.sendmail(username, args.to, args.message)
