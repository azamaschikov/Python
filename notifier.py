#!/usr/bin/env python

import os
import sys
import time
import requests

current_time = time.strftime('%a %b %d %T %Z')

def send_message(text):
    chat_id = 'your_chat_id'
    bot_id = 'your_bot_id'

    response = requests.post('https://api.telegram.org/bot' + bot_id + '/sendMessage', data={'chat_id':chat_id, 'text':text})
    response = response.json()

if sys.argv[1] == '--cpu':
    send_message('CPU is is exceeded')

if sys.argv[1] == '--memory':
    send_message('RAM is is exceeded')

if sys.argv[1] == '--io-disk':
    send_message('IO-disks is is exceeded')
