class Schedule(object):
    """Schedules in zaigen serve to update weights.
    They must define an update method to apply to
    the weight of an edge.
    """

    def __init__(self):
        pass

    def update(self, value):
        return value

class ConstantRate(Schedule):

    def __init__(self, rate):
        self.rate = rate

    def update(self, value):
        return self.rate*value

class PiecewiseRate(Schedule):

    def __init__(self, rate):
        self.rate = rate
        self.step = 0

    def update(self, value):
        value = self.rate[self.step]*value
        self.step += 1
        return value

class CompositeSchedule(Schedule):

    def __init__(self, schedule1, schedule2):
        self.schedules = [schedule1, schedule2]

    def update(self, value):
        for schedule in self.schedules:
            value = schedule.update(value)
        return value
