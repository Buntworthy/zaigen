import zaigen

class Weight(object):

	def __init__(self):
		self.value = 0
		self.pre_update = False
		self.schedule = zaigen.schedules.Schedule()

	def update(self, edge):
		self.value = self.schedule.update(self.value)

class Constant(Weight):

	def __init__(self, value):
		super(Constant, self).__init__()
		self.value = value

	def __repr__(self):
		return(f'Constant({self.value})')

class Interest(Weight):

	def __init__(self, rate):
		super(Interest, self).__init__()
		self.rate = rate
		self.pre_update = True

	def update(self, edge):
		self.value = self.rate*(edge.end_node.value)

	def __repr__(self):
		return(f'Interest({self.rate})')


class Remaining(Weight):

	def __init__(self, fraction):
		super(Remaining, self).__init__()
		self.fraction = fraction

	def update(self, edge):
		self.value = self.fraction*edge.start_node.value

	def __repr__(self):
		return(f'Remaining({self.fraction})')

class EdgeLinked(Weight):

	def __init__(self, rate, edge):
		super(EdgeLinked, self).__init__()
		self.rate = rate
		self.edge = edge

	def update(self, edge):
		self.value = self.rate*self.edge.weight.value

	def __repr__(self):
		return(f'EdgeLinked({self.rate}, {self.edge})')
