from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
import _sqlite3
import requests


driver = webdriver.Chrome()

driver.get("https://realty.ya.ru/otsenka-kvartiry-po-adresu-onlayn/?address=%25D0%25BF%25D1%2580%25D0%25BE%25D1%2581%25D0%25BF%25D0%25B5%25D0%25BA%25D1%2582%2520%25D0%259D%25D0%25B5%25D0%25BF%25D0%25BE%25D0%25BA%25D0%25BE%25D1%2580%25D1%2591%25D0%25BD%25D0%25BD%25D1%258B%25D1%2585%252C74&offerCategory=APARTMENT&offerType=SELL")

time.sleep(5)

element = driver.find_element(By.CLASS_NAME, 'OffersArchiveSearchOffers__body')

element_text = element.text

values = element_text.split('\n')

data_dict = {'descr':[], 'floor':[], 'price_1':[], 'per_m2_1':[], 'price_2':[],  'per_m2_2':[],  'opn_dt':[], 'lenght':[], 'cls_dt':[] }

for i in range(0,len(values),9) :
    data_dict['descr'].append (values[i])

for i in range(1,len(values),9) :
    data_dict['floor'].append (values[i])

for i in range(2,len(values),9) :
    data_dict['price_1'].append (values[i])

for i in range(3,len(values),9) :
    data_dict['per_m2_1'].append (values[i])

for i in range(4,len(values),9) :
    data_dict['price_2'].append (values[i])

for i in range(5,len(values),9) :
    data_dict['per_m2_2'].append (values[i])

for i in range(6,len(values),9) :
    data_dict['opn_dt'].append (values[i])

for i in range(7,len(values),9) :
    data_dict['lenght'].append (values[i])

for i in range(8,len(values),9) :
    data_dict['cls_dt'].append (values[i])

# Закрываем браузер
driver.quit()

for i in range(len(data_dict)):
    if data_dict['cls_dt'][i] == 'В продаже':
        text = f"""
        {data_dict['descr'][i]} || {data_dict['floor'][i]} || {data_dict['price_1'][i]} || {data_dict['per_m2_1'][i]} || {data_dict['price_2'][i]} 
        {data_dict['per_m2_2'][i]} ||  {data_dict['opn_dt'][i]} || {data_dict['lenght'][i]} || {data_dict['cls_dt'][i]} 
        """

        # Для телеги
        text = text
        chat_id = 404876596
        token = '6645356283:AAG6aKySdARzVnr3_6mkIaQ1NzEy-0m7zDc'
        url = 'https://api.telegram.org/bot6645356283:AAG6aKySdARzVnr3_6mkIaQ1NzEy-0m7zDc/sendMessage'
        data = {
            'chat_id':chat_id,
            'text':text,
            'parse_mode':'HTML'
        }
        response = requests.post(url=url, data=data)





