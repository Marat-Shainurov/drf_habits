from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDeleteAPIView, \
    AuxiliaryHabitListAPIView, AuxiliaryHabitCreateAPIView, AuxiliaryHabitUpdateAPIView, AuxiliaryHabitDeleteAPIView
from habits.views.reward_views import RewardViewSet

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'habits/rewards/', RewardViewSet, basename='rewards')


urlpatterns = [
    # main habits
    path('habits/', HabitListAPIView.as_view(), name='habits_list'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habits_create'),
    path('habits/update/<int:pk>', HabitUpdateAPIView.as_view(), name='habits_update'),
    path('habits/delete/<int:pk>', HabitDeleteAPIView.as_view(), name='habits_delete'),

    # auxiliary habits
    path('habits/auxiliary-habits/', AuxiliaryHabitListAPIView.as_view(), name='auxiliary_habits_list'),
    path('habits/auxiliary-habits/create/', AuxiliaryHabitCreateAPIView.as_view(), name='auxiliary_habits_create'),
    path('habits/auxiliary-habits/update/<int:pk>', AuxiliaryHabitUpdateAPIView.as_view(),
         name='auxiliary_habits_update'),
    path('habits/auxiliary-habits/delete/<int:pk>', AuxiliaryHabitDeleteAPIView.as_view(),
         name='auxiliary_habits_delete'),

    # rewards - via ViewSet endpoints
] + router.urls
