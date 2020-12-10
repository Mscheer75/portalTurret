#! /usr/bin/python
import requests


def send_message():
    return requests.post(
        "https://api.mailgun.net/v3/ ap key .mailgun.org/messages",
        auth=("api", " api key"),
        data={"from": "the turret <mailgun@ stuff .mailgun.org>",
            "to": [" email "],
            "subject": "Target found",
            "text": "intruder is at your door being shot"})


