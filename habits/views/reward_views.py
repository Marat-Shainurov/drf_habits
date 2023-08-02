from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from habits.models import Reward
from habits.paginators import RewardPagination
from habits.permissions import IsMainHabitOwner
from habits.serializers import RewardSerializer
from habits.serializers.reward_serializers import RewardCreateSerializer


class RewardViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for the Reward model.
    Serializers - RewardSerializer, RewardCreateSerializer, RewardShortSerializer.
    Pagination params - 3 objects per page, max_page_size - 10, page_size_query_param - 'page_size'.
    Permissions - IsAuthenticated, IsMainHabitOwner for 'retrieve', 'update', 'partial_update', 'destroy' methods.
        IsAuthenticated for the rest of the methods.
    """
    default_serializer = RewardSerializer
    queryset = Reward.objects.all()
    serializers = {
        'create': RewardCreateSerializer
    }
    pagination_class = RewardPagination

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMainHabitOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
