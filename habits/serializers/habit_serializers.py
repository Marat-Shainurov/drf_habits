from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from habits.models import Habit, AuxiliaryHabit, Reward
from habits.serializers import AuxiliaryHabitShortSerializer, RewardShortSerializer
from habits.validators import IsTooLong


class HabitSerializer(serializers.ModelSerializer):
    has_auxiliary_habits = SerializerMethodField()
    auxiliary_habit = AuxiliaryHabitShortSerializer(read_only=True, many=True)
    has_reward = SerializerMethodField()
    habit_reward = RewardShortSerializer(read_only=True, many=True)

    class Meta:
        model = Habit
        fields = ('id', 'name', 'user', 'action', 'action_time', 'action_place', 'duration', 'regularity', 'is_public',
                  'has_auxiliary_habits', 'auxiliary_habit', 'has_reward', 'habit_reward',)
        validators = [IsTooLong(field='duration')]


    def get_has_auxiliary_habits(self, habit):
        if AuxiliaryHabit.objects.filter(main_habit=habit).exists():
            return True
        return False

    def get_has_reward(self, habit):
        if Reward.objects.filter(main_habit=habit).exists():
            return True
        return False
