import datetime
import logging

import requests
from django.conf import settings
from django.shortcuts import get_object_or_404

from habits.models import Habit
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
              f'\nHere is a friendly reminder about your tomorrow\'s activities:\n' \
              f'\n- {output_coming_activities(chat_id)}' \
              f'\n\nHave a great and effective day!'

    req = requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}',
    )
    logger.info(f"Status Code: {req.status_code}, Response Text: {req.text}")


def send_greetings(chat_id):
    token = settings.TELEGRAM_API_TOKEN
    user = CustomUser.objects.get(chat_id=chat_id)

    message = f'{user.telegram}, \nHello and welcome!' \
              f'\nNow the work on your good habits will be even more effective!' \
              f'\nWe will send you daily friendly reminders about your next day activities.' \
              f'\nGood luck!'

    req = requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}',
    )

    logger.info(f"Joined user: {user.telegram}, Status Code: {req.status_code}, Response Text: {req.text}")

def output_coming_activities(chat_id):
    now_dow = datetime.datetime.now().isoweekday()

    user = get_object_or_404(CustomUser, chat_id=chat_id)
    user_habits = Habit.objects.filter(user=user)

    res = []
    for h in user_habits:
        h_regularity = h.regularity
        h_dow = h.days_of_week

        if h_regularity == 'daily':
            res.append(h.name + ' - ' + h.action_place + ' - ' + str(h.action_time))
        else:
            if str(int(now_dow) + 1) in h_dow:
                res.append(h.name + ' - ' + h.action_place + ' - ' + str(h.action_time))
    return "\n- ".join(res)