from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
import _sqlite3
import requests

def send_message(data_dict):
    text = data_dict
    chat_id = 404876596
    token = '6645356283:AAG6aKySdARzVnr3_6mkIaQ1NzEy-0m7zDc'
    url = 'https://api.telegram.org/bot6645356283:AAG6aKySdARzVnr3_6mkIaQ1NzEy-0m7zDc/sendMessage'
    data = {
        'chat_id':chat_id,
        'text':text,
        'parse_mode':'HTML'
    }
    response = requests.post(url=url, data=data)
    print(response)

data_dict = '1'
send_message(data_dict)









