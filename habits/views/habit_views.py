from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitListPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer, HabitCreateSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/create/

    - Creates the Habit model's objects.
    - Assigns the 'user' field as the request.user while the object's creation.
    - serializer_class - HabitCreateSerializer.
    - permission_classes - IsAuthenticated.

    - Params:
        name - required, str
        action - nullable, str
        action_time - required, TimeField (e.g., '18:00:00')
        action_place - required, str
        duration - required, ISO 8601 (max 2 minutes for a new habit - 'PT2M' in ISO 8601)
        regularity - nullable, str, a choice between 'daily' or 'weekly'. Default value - 'daily'
        days_of_week - required if the 'regularity' mode is 'weekly'. Can't be set when the regularity mode is 'daily'.
            A list of days should be passed (e.g. ['1', '2', '5'], where 1-7 are days of the week, from Monday to Sunday).
        is_public - nullable, boolean, False by default
        auxiliary_habit - an AuxiliaryHabit model object can be created
            (see the http://127.0.0.1:8000/habits/auxiliary-habits/create/ endpoint for more details)
        habit_reward - a Reward model object can be created
            (see the (see the http://127.0.0.1:8000/habits/rewards/ endpoint for more details) endpoint)
    """
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/
    - Returns a paginated list of the Habit model's objects.
    - Pagination params - 5 objects per page, max_page_size - 50, page_size_query_param - 'page_size'.
    - Returns all the request.user's instances (both is_public=True and is_public=False) and is_public=True for other users' objects.
    - serializer_class - HabitSerializer.
    - permission_classes - IsAuthenticated.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitListPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.filter(Q(user=user) | Q(is_public=True))
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/detail/<int:pk>/
    - Returns the Habit model's object.
    - serializer_class - HabitSerializer.
    - permission_classes - IsAuthenticated, IsOwner
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/update/<int:pk>/

    - Works both for PUT and PATCH methods. Updates the Habit model's object.
    - serializer_class - HabitSerializer.
    - permission_classes - IsAuthenticated, IsOwner.
    - Params set is similar to the creation one.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """
    Endpoint: http://127.0.0.1:8000/habits/delete/<int:pk>/

    - Deletes the Habit model's object.
    - serializer_class - HabitSerializer.
    - permission_classes - IsAuthenticated, IsOwner.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
