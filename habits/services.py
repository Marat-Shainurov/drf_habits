import logging

import requests
from django.conf import settings

from users.models import CustomUser

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("log.txt")
logger.addHandler(file_handler)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)


def get_user_chat_id(telegram_username):
    api_url = f"https://api.telegram.org/bot{settings.TELEGRAM_API_TOKEN}/getUpdates"
    response = requests.get(api_url)
    data = response.json()
    if data['ok'] and data['result']:
        for update in data['result']:
            if 'message' in update and 'from' in update['message']:
                if telegram_username[1:] == update['message']['from']['username']:
                    chat_id = update['message']['from']['id']
                    return chat_id
    else:
        return None


def set_chat_id_to_user(chat_id, telegram_username):
    user = CustomUser.objects.get(telegram=telegram_username)
    user.chat_id = chat_id
    user.save()


def send_habits_reminder(chat_id):
    token = settings.TELEGRAM_API_TOKEN
    user = CustomUser.objects.get(chat_id=chat_id)

    message = f'Hello, dear {user.telegram}!' \
              f'Here is a friendly reminder about your tomorrow\'s activities:' \
              f'{output_coming_activities()}'

    req = requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}',
    )
    logger.info(f"Status Code: {req.status_code}, Response Text: {req.text}")


def send_greetings(chat_id):
    token = settings.TELEGRAM_API_TOKEN
    user = CustomUser.objects.get(chat_id=chat_id)

    message = f'{user.telegram}, \nHello and welcome!' \
              f'\nNow the work on your good good habits would be even more effective!' \
              f'\nWe will send you daily friendly reminders about your next day activities.' \
              f'\nGood luck!'

    req = requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}',
    )

    logger.info(f"Joined user: {user.telegram}, Status Code: {req.status_code}, Response Text: {req.text}")

def output_coming_activities():
    return 'Activities outputted by a function!'