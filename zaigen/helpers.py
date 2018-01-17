import zaigen

def add_salary(graph, name, value):
	graph.add_node(zaigen.Node('in'))
	graph.add_edge(zaigen.Edge(name, 
								graph.get_node('in'), 
								graph.current_node, 
								value))
	

def add_pension(graph, rate, salary_edge, contrib_rate, interest_rate):
	pension_pot = zaigen.Node('pension_pot')
	interest_in_node = zaigen.Node('interest_in')
	pension_contrib_node = zaigen.Node('pension_contrib')

	graph.add_node(pension_pot)
	graph.add_node(interest_in_node)
	graph.add_node(pension_contrib_node)
	# Make sure to add the edges in the right order
	graph.add_edge(zaigen.Edge('pension_payment', 
								graph.current_node, 
								pension_pot, 
								zaigen.weights.Remaining(rate)))
	graph.add_edge(zaigen.Edge('interest', 
								interest_in_node, 
								pension_pot, 
								zaigen.weights.Interest(0.02)))
	graph.add_edge(zaigen.Edge('pesnion_contrib', 
								pension_contrib_node, 
								pension_pot, 
								zaigen.weights.EdgeLinked(contrib_rate, salary_edge)))
	add_transfer(graph)
	
def add_transfer(graph):
	new_end_node = zaigen.Node('inter')
	graph.add_node(new_end_node)
	graph.add_edge(zaigen.Edge('transfer', 
								graph.current_node, 
								new_end_node, 
								zaigen.weights.Remaining(1)))
	graph.current_node = new_end_node

	
def add_expense(graph, value):
	expense_out = zaigen.Node('expense_out')

	graph.add_node(expense_out)
	graph.add_edge(zaigen.Edge('expense', 
								graph.current_node, 
								expense_out, 
								zaigen.weights.Constant(value)))
	add_transfer(graph)

def add_tax(graph, rate):
	tax_out = zaigen.Node('tax_out')

	graph.add_node(tax_out)
	graph.add_edge(zaigen.Edge('tax', 
								graph.current_node, 
								tax_out, 
								zaigen.weights.Remaining(rate)))
	add_transfer(graph)