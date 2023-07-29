from .habit_views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDeleteAPIView
from .auxiliary_habit_views import AuxiliaryHabitCreateAPIView, AuxiliaryHabitDeleteAPIView, \
    AuxiliaryHabitUpdateAPIView, AuxiliaryHabitListAPIView

__all__ = [
    'HabitListAPIView', 'HabitCreateAPIView', 'HabitUpdateAPIView', 'HabitDeleteAPIView', 'AuxiliaryHabitCreateAPIView',
    'AuxiliaryHabitDeleteAPIView', 'AuxiliaryHabitUpdateAPIView', 'AuxiliaryHabitListAPIView',
]
