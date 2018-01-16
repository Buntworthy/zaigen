from graphviz import Digraph

def show(graph):
	dot = Digraph(comment='zaigen graph')
	for node in graph.nodes:
		dot.node(node.name, node.name)
	for edge in graph.edges:
		dot.edge(edge.start_node.name, 
					edge.end_node.name,
					label=edge.name)

	dot.view()