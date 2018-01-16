import zaigen

def add_pension(graph, last_node, rate):
	pension_pot = zaigen.Node('pension_pot')
	graph.add_node(pension_pot)
	graph.add_edge(zaigen.Edge('pension_payment', 
								last_node, 
								pension_pot, 
								zaigen.Remaining(0.06)))