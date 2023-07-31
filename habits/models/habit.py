from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Habit(models.Model):

    REGULARITY_CHOICES = [
        ('daily', 'Daily'),
        ('twice_a_week_MT', 'Twice a week (Mon + Thu)'),
        ('twice_a_week_TF', 'Twice a week (Tue + Fri)'),
        ('twice_a_week_WS', 'Twice a week (Wed + Sat)'),
        ('three_times_a_week_MWF', 'Three times a week (Mon + Wed + Fri)'),
        ('three_times_a_week_TTS', 'Three times a week (Tue + Thu + Sat)'),
        ('three_times_a_week_WFS', 'Three times a week (Wed + Fri + Sun)'),
        ('on_weekdays', 'From Monday to Friday'),
        ('on_weekends', 'From Saturday to Sunday'),
        ('each_mon', "Every Monday"),
        ('each_tue', "Every Tuesday"),
        ('each_wed', "Every Wednesday"),
        ('each_thu', "Every Thursday"),
        ('each_fri', "Every Friday"),
        ('each_sat', "Every Saturday"),
        ('each_sun', "Every Sunday"),
    ]

    name = models.CharField(verbose_name='habit_name', unique=True, max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.SET_NULL,
                             related_name='user_habits', **NULLABLE)
    action = models.TextField(verbose_name='action_description', **NULLABLE)
    action_time = models.TimeField(verbose_name='action_time')
    action_place = models.CharField(verbose_name='action_place', max_length=50)
    duration = models.DurationField(verbose_name='habit_duration')
    regularity = models.CharField(verbose_name='habit_regularity', choices=REGULARITY_CHOICES, default='daily',
                                  max_length=23)
    is_public = models.BooleanField(default=False, verbose_name='is_habit_public')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Main habit'
        verbose_name_plural = 'Main habits'
