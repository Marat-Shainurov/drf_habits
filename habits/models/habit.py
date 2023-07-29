from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Habit(models.Model):

    REGULARITY_CHOICES = [
        ('daily', 'Daily'),
        ('twice_a_week', 'Twice a week'),
        ('weekly', 'Weekly'),
    ]

    name = models.CharField(verbose_name='habit_name', unique=True, max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.SET_NULL,
                             related_name='user', **NULLABLE)
    action = models.TextField(verbose_name='action_description', **NULLABLE)
    action_time = models.DateTimeField(verbose_name='action_time')
    action_place = models.CharField(verbose_name='action_place', max_length=50)
    duration = models.DurationField(verbose_name='habit_duration')
    regularity = models.CharField(verbose_name='habit_regularity', choices=REGULARITY_CHOICES, default='daily',
                                  max_length=13)
    is_public = models.BooleanField(default=False, verbose_name='is_habit_public')
    has_auxiliary_habits = models.BooleanField(verbose_name='has_auxiliary_habits', default=False)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Main habit'
        verbose_name_plural = 'Main habits'
