# General Description
drf_habits is a django-rest-framework project.
The project is created for working on the users personal efficiency and good habits.

# Install and usage
1. Clone the project from https://github.com/Marat-Shainurov/drf_habits to your local machine.
2. Build a new image and run the project container from the root project directory:
    - docker-compose build
    - docker-compose up
3. Read the project's documentation (swagger or redoc format):
    - http://127.0.0.1:8000/swagger/
    - http://127.0.0.1:8000/redoc/
4. Go to the main page on your browser http://127.0.0.1:8000/ and start working with the app's endpoints.

# Apps and models
1. habits - habits model.
   Habit - main habit model. Each habit can have either an auxiliary habit or a reward (to support a main habit execution).
   AuxiliaryHabit - additional/extra habit model (to support the main one).
   Reward - reword model (for a main habit execution).
2. users - users model.
   CustomUser - customized users model.
   UersManager class is overridden and customized as well (drf_habits/users/manager.py)

# Integration with Telegram
Integration with Telegram is created for communication with the application's users over the Telegram chatbot ('HabitBot').
Periodic tasks getUpdate_bot and send_daily_reminders are set in setting.py and ./habits/tasks.py.
Subscribe to  HabitBot:
- find the Telegram chatbot (@ms_habits_bot)
- click /start' \
  A greeting message will be sent within 5 seconds.\
  After that, the subscribed user will receive daily reminders at 19.00
  about tomorrow's habits to be executed.

# Testing
- All the habits endpoints are covered by pytest tests in habits/tests
- Run tests:\
  docker-compose exec app python manage.py test
