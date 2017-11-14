#!/usr/local/bin/python

import time
import re
import json
import traceback
from slackclient import SlackClient
import datetime
import netifaces as ni

from config import api_key, interface, request_name, bot_name

while True:
    try:
        slack_client = SlackClient(api_key)

        # Fetch your Bot's User ID
        user_list = slack_client.api_call("users.list")
        for user in user_list.get('members'):
            if user.get('name') == bot_name:
                slack_user_id = user.get('id')
                break

        # Start connection
        if slack_client.rtm_connect():
            print "Connected!"
            today = datetime.date.today()
            print str(today)
            print ""

            while True:
                for message in slack_client.rtm_read():
                    starts = "<@%s> " + request_name
                    starts2 = "<@%s> list"
                    if 'text' in message and message['text'].startswith(starts2 % slack_user_id):
                        today = datetime.date.today()
                        print str(today)

                        print "Message received: %s" % json.dumps(message, indent=2)
                        print ""

                        out = request_name
                        slack_client.api_call(
                            "chat.postMessage",
                            channel=message['channel'],
                            text=out,
                            as_user=True)

                    if 'text' in message and message['text'].startswith(starts % slack_user_id):
                        today = datetime.date.today()
                        print str(today)

                        print "Message received: %s" % json.dumps(message, indent=2)
                        print ""

                        out = ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']

                        slack_client.api_call(
                            "chat.postMessage",
                            channel=message['channel'],
                            text=out,
                            as_user=True)
                time.sleep(1)

    except Exception as e:
        print("ERROR")
        today = datetime.date.today()
        print str(today)
        print(e)
        print()
        traceback.print_exc()
        print()
