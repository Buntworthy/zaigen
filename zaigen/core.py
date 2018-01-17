import zaigen

class Graph(object):
	
	def __init__(self):
		self.nodes = []
		self.edges = []

	def add_node(self, node):
		self.nodes.append(node)

	def get_node(self, node_name):
		matching_nodes = [node for node in self.nodes if node.name == node_name]
		return matching_nodes[0]

	def add_edge(self, edge):
		self.edges.append(edge)

	def update(self):
		self.reset()
		self.update_pre_edges()
		self.main_update()

	def reset(self):
		for node in self.nodes:
			node.reset()
		for edge in self.edges:
			edge.reset()

	def main_update(self):
		# Bredth first update
		while not self.updated:
			nodes_to_update = [node 
				for node in self.nodes 
					if node.current_in_degree==0
					and not node.updated]
			for node in nodes_to_update:
				node.update()

	def update_pre_edges(self):
		pre_update_edges = (edge for edge in self.edges if edge.pre_update)
		for edge in pre_update_edges:
			edge.update()

	@property
	def updated(self):
		if (all((node.updated for node in self.nodes)) and
			all((edge.updated for edge in self.edges))):
			return True
		else:
			return False

	def __str__(self):
		info_string = 'Zaigen graph\n'
		info_string += '\tNodes:\n'
		for node in self.nodes:
			node_string = node.__repr__()
			info_string += '\t\t' + node_string + '\n'
		info_string += '\tEdges:\n'
		for edge in self.edges:
			edge_string = edge.__repr__()
			info_string += '\t\t' + edge_string + '\n'
		return info_string

class Node(object):
	"""Basic node data structure for money graph"""

	def __init__(self, name):
		self.name = name
		self.upstream_nodes = []
		self.downstream_nodes = []
		self.edge_list = []
		self.value = 0
		self.updated = False
		self.current_in_degree = self.in_degree
		self.history = [self.value]

	def update(self):
		for node in self.downstream_nodes:
			for edge in node.edge_list:
				if edge.start_node is self and not edge.updated:
					edge.update()
			node.current_in_degree -= 1
		self.updated = True
		self.history.append(self.value)

	def reset(self):
		self.updated = False
		self.current_in_degree = self.in_degree

	@property
	def in_degree(self):
		return len(self.upstream_nodes)

	def __repr__(self):
		return f'Node(name=\'{self.name}\')'

class Edge(object):
	"""Basic edge data structure for money graph"""
	
	def __init__(self, name, start_node, end_node, weight):
		self.name = name
		self.start_node = start_node
		self.end_node = end_node
		self.updated = False
		self.applied = False
		if isinstance(weight, (int, float)):
			self.weight = zaigen.weights.Constant(weight)
		else:
			self.weight = weight
		self.history = [self.weight.value]
		self.start_node.edge_list.append(self)
		self.end_node.edge_list.append(self)
		self.start_node.downstream_nodes.append(self.end_node)
		self.end_node.upstream_nodes.append(self.start_node)

	def update(self):
		self.weight.update(self)
		self.start_node.value -= self.weight.value
		self.end_node.value += self.weight.value
		self.history.append(self.weight.value)
		self.updated = True

	def reset(self):
		self.updated = False
		
	@property
	def pre_update(self):
		return self.weight.pre_update

	def __repr__(self):
		return f'Edge(name=\'{self.name}\', ' \
						f'start_node=\'{self.start_node.name}\', ' \
						f'end_node=\'{self.end_node.name}\', ' \
						f'weight={self.weight})'

if __name__ == '__main__':
	g = Graph()
	g.add_node(Node('Node 1'))
	g.add_node(Node('Node 2'))
	g.add_node(Node('Node 3'))
	g.add_node(Node('Node 4'))

	g.add_edge(Edge('Edge 1', 
				start_node=g.get_node('Node 1'), 
				end_node=g.get_node('Node 2'), 
				weight=100))

	g.add_edge(Edge('Edge 2', 
				start_node=g.get_node('Node 1'), 
				end_node=g.get_node('Node 3'), 
				weight=100))

	g.add_edge(Edge('Edge 3', 
				start_node=g.get_node('Node 2'), 
				end_node=g.get_node('Node 3'), 
				weight=100))

	print(g)
	g.update()