from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import AuxiliaryHabit
from habits.paginators import HabitListPagination
from habits.permissions import IsMainHabitOwner
from habits.serializers import AuxiliaryHabitSerializer, AuxiliaryHabitCreateSerializer


class AuxiliaryHabitCreateAPIView(generics.CreateAPIView):
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitCreateSerializer
    permission_classes = [IsAuthenticated]


class AuxiliaryHabitListAPIView(generics.ListAPIView):
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer
    pagination_class = HabitListPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = AuxiliaryHabit.objects.filter(Q(main_habit__user=user) | Q(is_public=True))
        return queryset


class AuxiliaryHabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer
    permission_classes = [IsAuthenticated, IsMainHabitOwner]


class AuxiliaryHabitUpdateAPIView(generics.UpdateAPIView):
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer
    permission_classes = [IsAuthenticated, IsMainHabitOwner]


class AuxiliaryHabitDeleteAPIView(generics.DestroyAPIView):
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer
    permission_classes = [IsAuthenticated, IsMainHabitOwner]
