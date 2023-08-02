from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habits.models import AuxiliaryHabit


class AuxiliaryHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxiliaryHabit
        fields = ('id', 'main_habit', 'name', 'action', 'action_time', 'action_place', 'duration', 'is_public')


class AuxiliaryHabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxiliaryHabit
        fields = '__all__'

    def create(self, validated_data):
        habit = validated_data.get('main_habit')
        if not habit:
            raise ValidationError(
                {"result":
                     "For a separate AuxiliaryHabit object creation you have to specify the 'main_habit' filed value. "
                     "Please pass the 'main_habit pk' there."
                 }
            )
        if habit.habit_reward.all().exists():
            raise ValidationError({
                "result": 'This habit already has a reward! You can assign either a reward or an auxiliary habit'})
        return super().create(validated_data)


class AuxiliaryHabitShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxiliaryHabit
        fields = ('name', 'action',)
