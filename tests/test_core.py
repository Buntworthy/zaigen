from .context import zaigen

def test_edges():

	n1 = zaigen.Node('Node 1')
	n2 = zaigen.Node('Node 2')
	e1 = zaigen.Edge('Edge 1', 
				start_node=n1, 
				end_node=n2, 
				weight=100)

	assert n2 in e1.start_node.downstream_nodes
	assert n1 in e1.end_node.upstream_nodes

def test_graph_add_nodes():

	g = zaigen.Graph()
	n1 = zaigen.Node('Node 1')
	n2 = zaigen.Node('Node 2')

	g.add_node(n1)
	g.add_node(n2)

	assert n1 in g.nodes
	assert n2 in g.nodes

def test_graph_get_nodes():

	g = zaigen.Graph()
	n1 = zaigen.Node('Node 1')
	n2 = zaigen.Node('Node 2')

	g.add_node(n1)
	g.add_node(n2)

	assert n1 == g.get_node('Node 1')
	assert n2 == g.get_node('Node 2')

def test_graph_add_edges():
	

	g = zaigen.Graph()
	n1 = zaigen.Node('Node 1')
	n2 = zaigen.Node('Node 2')
	e1 = zaigen.Edge('Edge 1', 
				start_node=n1, 
				end_node=n2, 
				weight=100)

	g.add_node(n1)
	g.add_node(n2)
	g.add_edge(e1)

	assert e1 in g.edges

def test_update_graph():

	g = zaigen.Graph()
	n_in = zaigen.Node('in')
	n_out = zaigen.Node('out')
	e1 = zaigen.Edge('transfer', 
				start_node=n_in, 
				end_node=n_out, 
				weight=100)

	g.add_node(n_in)
	g.add_node(n_out)
	g.add_edge(e1)

	assert n_out.value == 0

	g.update()

	assert n_out.value == 100

	g.reset()

	assert n_out.value == 100

	g.update()
	
	assert n_out.value == 200