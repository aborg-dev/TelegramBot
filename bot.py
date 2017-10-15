#!/usr/bin/env python

import requests
import json
import datetime
import time
import argparse
import os

from yandex_translate import YandexTranslate


class BotHandler(object):
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        params = {"timeout": timeout, "offset": offset}
        resp = requests.get(self.api_url + "getUpdates", params)
        return resp.json()["result"]

    def send_message(self, chat_id, text):
        params = {"chat_id": chat_id, "text": text}
        return requests.post(self.api_url + "sendMessage", params)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", type=str, default="")
    parser.add_argument("--yandex_api_key", type=str, default="")
    args = parser.parse_args()

    token = args.token
    if not token:
        if not "TELEGRAM_TOKEN" in os.environ:
            print(
                "Please, set bot token through --token or TELEGRAM_TOKEN env variable"
            )
            return
        token = os.environ["TELEGRAM_TOKEN"]

    if not args.yandex_api_key:
        print("Please, set Yandex API key")
        return
    translate = YandexTranslate(args.yandex_api_key)

    bot = BotHandler(token)
    offset = 0

    while True:
        updates = bot.get_updates(offset=offset)
        for update in updates:
            print(update)
            chat_id = update["message"]["chat"]["id"]
            if "text" in update["message"]:
                text = update["message"]["text"]
                source_lang = translate.detect(text)
                if source_lang == "en":
                    dest_lang = "ru"
                else:
                    dest_lang = "en"

                translated = translate.translate(text, dest_lang)
                if "text" in translated:
                    bot.send_message(chat_id, translated["text"])
            offset = max(offset, update["update_id"] + 1)

        time.sleep(1)



if __name__ == "__main__":
    main()
