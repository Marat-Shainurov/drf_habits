from rest_framework import serializers

from habits.models import AuxiliaryHabit
from habits.validators import HasReward


class AuxiliaryHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxiliaryHabit
        fields = ('id', 'main_habit', 'name', 'action', 'action_time', 'action_place', 'duration', 'is_public')


class AuxiliaryHabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxiliaryHabit
        fields = '__all__'
        validators = [HasReward(field='main_habit')]


class AuxiliaryHabitShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxiliaryHabit
        fields = ('name', 'action',)
