from rest_framework import serializers

from habits.models import AuxiliaryHabit


class AuxiliaryHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxiliaryHabit
        fields = ('main_habit', 'name', 'action', 'action_time', 'action_place', 'duration', 'is_public')
