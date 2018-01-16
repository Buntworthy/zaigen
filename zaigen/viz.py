from graphviz import Digraph
import pygal

def show_graph(graph):
	dot = Digraph(comment='zaigen graph')
	for node in graph.nodes:
		dot.node(node.name, node.name)
	for edge in graph.edges:
		dot.edge(edge.start_node.name, 
					edge.end_node.name,
					label=edge.name)

	dot.view()

def plot_node(nodes):
	line_chart = pygal.Line()
	line_chart.title = 'Node value'
	for node in nodes:
		line_chart.add(node.name, node.history)
	line_chart.render_in_browser()

def plot_edge(edges):
	line_chart = pygal.Line()
	line_chart.title = 'Edge weight'
	for edge in edges:
		line_chart.add(edge.name, edge.history)
	line_chart.render_in_browser()