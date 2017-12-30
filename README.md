# TelegramBot

This repo guides you through a simple echo Telegram bot example.

## Local Setup

1. Register bot by talking to @BotFather, and save the token
2. Try out using this token to get updates at https://api.telegram.org/bot`TOKEN`/getUpdates
3. Try sending a message to https://api.telegram.org/bot`TOKEN`/sendMessage?chat_id=`ID`&text=`TEXT`
4. Get the code: `git clone https://github.com/akashin/TelegramBot.git`
5. Install dependencies: `pip install -r requirements.txt`
6. Run the bot with: `python bot.py`

## Heroku Setup
Complete the steps from the local setup and then:

1. Register on https://heroku.com
2. Install heroku command line interface https://devcenter.heroku.com/articles/heroku-cli
3. Create new Heroku application for our bot:
```sh
heroku login
heroku create --region eu appname # create app in eu region, common regions: eu, us
heroku buildpacks:set heroku/python # set python buildpack
git push heroku master # deploy app to heroku
heroku config:set TELEGRAM_TOKEN=123456789:AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLL # set config vars
heroku logs --tail # If for some reason it’s not working, check the logs
```

This should automatically start your bot on Heroku.

## Materials

- Good tutorial: http://djangostars.com/blog/how-to-create-and-deploy-a-telegram-bot/
- Useful Heroku commands: https://github.com/Kylmakalle/heroku-telegram-bot

