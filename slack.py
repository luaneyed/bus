import json
from urllib import request

from config import SLACK_CONFIG

webhook_url = 'https://hooks.slack.com/services/' + SLACK_CONFIG['webhook']


def log(message: str):
    slack_data = {'text': message}

    req = request.Request(
        webhook_url, data=json.dumps(slack_data).encode("utf-8"),
        headers={'Content-Type': 'application/json'}
    )

    request.urlopen(req)
