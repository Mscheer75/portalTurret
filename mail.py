#! /usr/bin/python
import requests


def send_message():
    return requests.post(
        "https://api.mailgun.net/v3//messages",
        auth=("api", "4879ff27-b1e850a6"),
        data={"from": 'hello@example.com',
            "to": ["crazyhalolad@gmail.com"],
            "subject": "You have a visitor",
            "html": "<html> intruder is at your door being shot  </html>"})


