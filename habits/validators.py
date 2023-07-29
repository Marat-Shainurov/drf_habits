from rest_framework.exceptions import ValidationError


class HasReward:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val.habit_reward.all():
            raise ValidationError(
                'This habit already has a reward! You can assign either a reward or an auxiliary habit.')


class HasAuxiliaryHabit:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val.auxiliary_habit.all():
            raise ValidationError(
                'This habit already has a linked auxiliary habit! You can assign either a reward or an auxiliary habit')
