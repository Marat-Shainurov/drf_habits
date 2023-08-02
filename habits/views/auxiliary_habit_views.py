from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import AuxiliaryHabit
from habits.paginators import HabitListPagination
from habits.permissions import IsMainHabitOwner
from habits.serializers import AuxiliaryHabitSerializer, AuxiliaryHabitCreateSerializer


class AuxiliaryHabitCreateAPIView(generics.CreateAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/auxiliary-habits/create/

    Creates the AuxiliaryHabit model's objects.
    serializer_class - AuxiliaryHabitCreateSerializer.
    permission_classes - IsAuthenticated.

    Params:
    name - required, str
    main_habit - required, int (the FK field of the main_habit. related_name - 'auxiliary_habit').
    action - nullable, str
    action_time - nullable, TimeField (e.g., '18:00:00')
    action_place - nullable, str
    duration - nullable, ISO 8601 (max 2 minutes for a new habit - 'PT2M' in ISO 8601)
    is_public - nullable, boolean, False by default
    """
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitCreateSerializer
    permission_classes = [IsAuthenticated]


class AuxiliaryHabitListAPIView(generics.ListAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/auxiliary-habits/

    Returns a paginated list of the AuxiliaryHabit model's objects.
    Pagination params - 5 objects per page, max_page_size - 50, page_size_query_param - 'page_size'.
    Returns all the main_habit object's request.user instances (both is_public=True and is_public=False),
    and is_public=True for other users' of main_habit objects.
    serializer_class - AuxiliaryHabitSerializer.
    permission_classes - IsAuthenticated.

    """
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer
    pagination_class = HabitListPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = AuxiliaryHabit.objects.filter(Q(main_habit__user=user) | Q(is_public=True))
        return queryset


class AuxiliaryHabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/auxiliary-habits/detail/<int:pk>/

    Returns the AuxiliaryHabit model's object.
    serializer_class - AuxiliaryHabitSerializer.
    permission_classes - IsAuthenticated, IsMainHabitOwner.
    """
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer
    permission_classes = [IsAuthenticated, IsMainHabitOwner]


class AuxiliaryHabitUpdateAPIView(generics.UpdateAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/auxiliary-habits/update/<int:pk>/

    Updates the AuxiliaryHabit model's object.
    serializer_class - AuxiliaryHabitSerializer.
    permission_classes - IsAuthenticated, IsMainHabitOwner.
    """
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer
    permission_classes = [IsAuthenticated, IsMainHabitOwner]


class AuxiliaryHabitDeleteAPIView(generics.DestroyAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/auxiliary-habits/delete/<int:pk>/

    Deletes the AuxiliaryHabit model's object.
    serializer_class - AuxiliaryHabitSerializer.
    permission_classes - IsAuthenticated, IsMainHabitOwner.
    """
    queryset = AuxiliaryHabit.objects.all()
    serializer_class = AuxiliaryHabitSerializer
    permission_classes = [IsAuthenticated, IsMainHabitOwner]
