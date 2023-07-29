from rest_framework import generics, viewsets

from habits.models import Reward
from habits.serializers import RewardSerializer
from habits.serializers.reward_serializers import RewardCreateSerializer


class RewardViewSet(viewsets.ModelViewSet):
    default_serializer = RewardSerializer
    queryset = Reward.objects.all()
    serializers = {
        'create': RewardCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
