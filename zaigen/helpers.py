import zaigen

def add_salary(graph, value):
	graph.add_node(zaigen.Node('in'))
	graph.add_edge(zaigen.Edge('salary-x', 
								graph.get_node('in'), 
								graph.current_node, 
								zaigen.weights.Constant(value)))
	

def add_pension(graph, rate, interest_rate):
	new_end_node = zaigen.Node('inter')
	pension_pot = zaigen.Node('pension_pot')
	in_node = zaigen.Node('in')
	graph.add_node(new_end_node)
	graph.add_node(pension_pot)
	graph.add_node(in_node)
	# Make sure to add the edges in the right order
	graph.add_edge(zaigen.Edge('pension_payment', 
								graph.current_node, 
								pension_pot, 
								zaigen.weights.Remaining(rate)))
	graph.add_edge(zaigen.Edge('interest-x', 
								in_node, 
								pension_pot, 
								zaigen.weights.Interest(0.02)))
	graph.add_edge(zaigen.Edge('transfer-x', 
								graph.current_node, 
								new_end_node, 
								zaigen.weights.Remaining(1)))
	graph.current_node = new_end_node