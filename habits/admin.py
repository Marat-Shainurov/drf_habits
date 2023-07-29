from django.contrib import admin

from habits.models import Habit, AuxiliaryHabit, Reward


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'action', 'action_time', 'action_place', 'duration', 'regularity', 'is_public',)


@admin.register(AuxiliaryHabit)
class AuxiliaryHabitAdmin(admin.ModelAdmin):
    list_display = ('main_habit', 'name', 'action', 'action_time', 'action_place', 'duration', 'is_public',)


@admin.register(Reward)
class RewardHabitAdmin(admin.ModelAdmin):
    list_display = ('main_habit', 'name', 'description', 'resources',)
