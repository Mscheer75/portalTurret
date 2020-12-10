#! /usr/bin/python
import requests


def send_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox286ad405f7fa4339a9aac3f8399cfaf5.mailgun.org/messages",
        auth=("api", "42ab66f261dc8b52dff6f3bc3e4ddf39-4879ff27-b1e850a6"),
        data={"from": "the turret <mailgun@sandbox286ad405f7fa4339a9aac3f8399cfaf5.mailgun.org>",
            "to": ["crazyhalolad@gmail.com"],
            "subject": "Target found",
            "text": "intruder is at your door being shot"})


