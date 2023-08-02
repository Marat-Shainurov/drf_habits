# drf_habits project

# Описание проекта
drf_habits это django-rest-framework проект.
Проект создан для работы над персональной эффективностью пользователей, для работы над полезными привычками.

# Приложения и модели
1. habits.
   Habit - основная привычка.
   AuxiliaryHabit - вспомогательная привычка.
   Reward - вознаграждение за выполнение основной привычки.
2. users.
   CustomUser - кастомная модель пользователей.
   Переопределен и кастомизирован также и UersManager класс (drf_habits/users/manager.py)

# Валидация
- Для основной привычки может быть создана либо вспомогательная привычка (auxiliary_habit), 
  либо вознаграждение (habit_reward). Валидация на уровне сериализаторов.
- Вознаграждение может быть присвоено только для основной привычки. Валидация на уровне моделей.
- Время выполнения новой привычки должно быть не больше 120 секунд. Валидация через кастомный валидатор.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней. Валидация на уровне поля модели и доступного выбора.

# Пагинация
Для вывода списка привычек реализована пагинацию с выводом по 5 привычек на страницу.
Для вывода списка вознаграждений реализована пагинацию с выводом по 3 вознаграждений на страницу.

# Права доступа
Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.
Кастомные permissions - IsOwner, IsMainHabitOwner.

# Эндпоинты и документация
Настроена документация yasg-drf.
Все эндпоинты можно изучить по ссылкам:
http://localhost:8000/redoc/
http://localhost:8000/swagger/

# Интеграции
Создана интеграция с API Telegram, для рассылок напоминаний.
Периодические задачи getUpdate_bot и send_daily_reminders настроены в setting.py и ./habits/tasks.py.
Подписаться на уведомления от чата HabitBot:
- найти в Telegram bot @ms_habits_bot
- нажать /start'. 
  В течении 5-10 секунд придет приветственное сообщение.
  Далее, ежедневно, в 19.00 пользователь будет получать напоминания о завтрашних привычках к исполнению.

# Безопасность
Для проекта настроен CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.
