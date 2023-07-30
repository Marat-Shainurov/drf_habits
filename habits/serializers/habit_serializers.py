from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField

from habits.models import Habit, AuxiliaryHabit, Reward
from habits.serializers import AuxiliaryHabitShortSerializer, RewardShortSerializer, AuxiliaryHabitCreateSerializer, \
    RewardCreateSerializer
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


class HabitCreateSerializer(serializers.ModelSerializer):

    habit_reward = RewardCreateSerializer(many=True, required=False)
    auxiliary_habit = AuxiliaryHabitCreateSerializer(many=True, required=False)

    class Meta:
        model = Habit
        fields = (
        'name', 'user', 'action', 'action_time', 'action_place', 'duration', 'regularity', 'is_public', 'habit_reward',
        'auxiliary_habit')

    def create(self, validated_data):

        habit_reward_data = validated_data.pop('habit_reward', [])
        auxiliary_habit_data = validated_data.pop('auxiliary_habit', [])
        main_habit = Habit.objects.create(**validated_data)

        if habit_reward_data and auxiliary_habit_data:
            raise ValidationError('You can assign either a reward or an auxiliary habit')

        for r in habit_reward_data:
            Reward.objects.create(main_habit=main_habit, **r)

        for h in auxiliary_habit_data:
            AuxiliaryHabit.objects.create(main_habit=main_habit, **h)

        return main_habit
