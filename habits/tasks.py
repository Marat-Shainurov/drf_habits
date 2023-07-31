from celery import shared_task

from habits.services import get_user_chat_id, set_chat_id_to_user, send_habits_reminder, logger
from users.models import CustomUser


@shared_task
def update_telegram_bot_activity():
    users = CustomUser.objects.all(is_active=True)

    no_id = []
    with_id = []

    for user in users:
        telegram_username = user.telegram
        if user.chat_id:
            chat_id = user.chat_id
            send_habits_reminder(chat_id)
            with_id.append(telegram_username)
        else:
            chat_id = get_user_chat_id(telegram_username)
            if chat_id:
                set_chat_id_to_user(chat_id, telegram_username)
                send_habits_reminder(chat_id)
                no_id.append(telegram_username + ' - ' + chat_id)

    logger.info(f"No id - {no_id}, \nWith id - {with_id}")