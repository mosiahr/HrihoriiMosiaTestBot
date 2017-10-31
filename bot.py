#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import misc
import json
from time import sleep

from yobit import get_btc


# 'https://api.telegram.org/bot380340276:AAGphWQv59oOyom2-yA0jlmRlzEKNHGP5lI/sendMessage?chat_id=202244402&text=hi'
token = misc.token
URL = 'https://api.telegram.org/bot{}/'.format(token)

global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
#   print(r.content)
    return r.json()


def get_message():
    # Отвечать только на новые сообщения
    # Получаем update_id, каждого обновления
    # записывать в переменную, а затем сравнивать его с update_id последнего элемента в
    # списке result

    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {
            'chat_id': chat_id,
            'text': message_text
        }

        return message
    return None


def send_message(chat_id, text='Wait a second, please...'):
    url = '{}sendmessage?chat_id={}&text={}'.format(URL, chat_id, text)
    requests.get(url)




def main():
    # d = get_updates()
    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)



    while True:
        answer = get_message()

        if answer:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/btc':
                send_message(chat_id, get_btc())
        else:
            continue

        sleep(2)


if __name__=='__main__':
    main()
