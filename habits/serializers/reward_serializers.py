from rest_framework import serializers

from habits.models import Reward
from habits.validators import HasAuxiliaryHabit


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'


class RewardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'
        validators = [HasAuxiliaryHabit(field='main_habit')]

class RewardShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('id', 'name',)

