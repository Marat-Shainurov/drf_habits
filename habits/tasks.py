from celery import shared_task

from habits.services import get_user_chat_id, set_chat_id_to_user, send_habits_reminder, logger, send_greetings
from users.models import CustomUser


@shared_task
def getUpdate_bot():
    users = CustomUser.objects.filter(is_active=True, chat_id__isnull=True)

    if users:
        for user in users:
            telegram_username = user.telegram
            chat_id = get_user_chat_id(telegram_username)
            if chat_id:
                set_chat_id_to_user(chat_id, telegram_username)
                send_greetings(chat_id)
                logger.info(f'New user {user.telegram} with chat_id {chat_id} is added to the chat bot and greeted')

@shared_task
def send_daily_reminders():
    users = CustomUser.objects.filter(is_active=True, chat_id__isnull=False)
    logger.info(f'users - {users}')

    if users:
        for user in users:
            chat_id = user.chat_id
            send_habits_reminder(chat_id)
            logger.info(f'{user.telegram} ({user.chat_id}) has been informed')
