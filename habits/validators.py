from rest_framework.exceptions import ValidationError


class HasReward:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.habit_reward.all().exists():
            raise ValidationError(
                'This habit already has a reward! You can assign either a reward or an auxiliary habit.')


class HasAuxiliaryHabit:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.auxiliary_habit.all().exists():
            raise ValidationError(
                'This habit already has a linked auxiliary habit! You can assign either a reward or an auxiliary habit')
