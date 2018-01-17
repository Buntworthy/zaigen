import zaigen

def add_salary(graph, value):
	in_node = zaigen.Node('in-x')
	new_end_node = zaigen.Node('inter-x')
	graph.add_edge(zaigen.Edge('salary-x', 
								in_node, 
								new_end_node, 
								zaigen.Constant(value)))
	

def add_pension(graph, last_node, rate):
	new_end_node = zaigen.Node('inter-x')
	pension_pot = zaigen.Node('pension_pot')
	graph.add_node(new_end_node)
	graph.add_node(pension_pot)
	# Make sure to add the edges in the right order
	graph.add_edge(zaigen.Edge('pension_payment', 
								last_node, 
								pension_pot, 
								zaigen.Remaining(rate)))
	graph.add_edge(zaigen.Edge('transfer-x', 
								last_node, 
								new_end_node, 
								zaigen.Remaining(1)))