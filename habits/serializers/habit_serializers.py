from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from habits.models import Habit, AuxiliaryHabit


class HabitSerializer(serializers.ModelSerializer):
    has_auxiliary_habits = SerializerMethodField()

    class Meta:
        model = Habit
        fields = ('name', 'user', 'action', 'action_time', 'action_place', 'duration', 'regularity', 'is_public',
                  'has_auxiliary_habits',)

    def get_has_auxiliary_habits(self, habit):
        if AuxiliaryHabit.objects.filter(main_habit=habit).exists():
            return True
        return False
