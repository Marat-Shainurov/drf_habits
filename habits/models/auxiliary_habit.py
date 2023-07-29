from django.db import models

from habits.models import Habit
from users.models import NULLABLE


class AuxiliaryHabit(models.Model):
    main_habit = models.ForeignKey(Habit, verbose_name='main_habit', related_name='auxiliary_habit',
                                   on_delete=models.SET_NULL, **NULLABLE)
    name = models.CharField(verbose_name='auxiliary_habit_name', max_length=50, unique=True)
    action = models.TextField(verbose_name='auxiliary_action_description', **NULLABLE)
    action_time = models.DateTimeField(verbose_name='auxiliary_action_time', **NULLABLE)
    action_place = models.CharField(verbose_name='auxiliary_action_place', max_length=50, **NULLABLE)
    duration = models.DurationField(verbose_name='auxiliary_habit_duration', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='is_auxiliary_habit_public')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Auxiliary habit'
        verbose_name_plural = 'Auxiliary habits'
