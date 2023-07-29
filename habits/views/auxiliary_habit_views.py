from rest_framework import generics

from habits.models import AuxiliaryHabit
from habits.serializers import AuxiliaryHabitSerializer, AuxiliaryHabitCreateSerializer


class AuxiliaryHabitCreateAPIView(generics.CreateAPIView):
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitCreateSerializer


class AuxiliaryHabitListAPIView(generics.ListAPIView):
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer


class AuxiliaryHabitUpdateAPIView(generics.UpdateAPIView):
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer


class AuxiliaryHabitDeleteAPIView(generics.DestroyAPIView):
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer
