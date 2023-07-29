from rest_framework import serializers

from habits.serializers import HabitSerializer
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'phone', 'telegram', 'avatar', 'last_login')

class CustomUserDetailSerializer(serializers.ModelSerializer):
    user_habits = HabitSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'phone', 'telegram', 'avatar', 'last_login', 'user_habits')