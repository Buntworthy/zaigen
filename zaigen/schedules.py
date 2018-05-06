import collections

class Schedule(object):
    """Schedules in zaigen serve to update weights.
    They must define an update method to apply to
    the weight of an edge.
    """

    def __init__(self):
        pass

    def update(self, value):
        return value

class Rate(Schedule):

    def __init__(self, rate):
        if not isinstance(rate, collections.Iterable):
            self.rate = [rate]
        else:
            self.rate = rate
        self.index = 0

    def update(self, value):
        value = self.rate[self.index]*value
        if self.index < len(self.rate) - 1:
            self.index += 1
        return value


class CompositeSchedule(Schedule):

    def __init__(self, schedule1, schedule2):
        self.schedules = [schedule1, schedule2]

    def update(self, value):
        for schedule in self.schedules:
            value = schedule.update(value)
        return value
