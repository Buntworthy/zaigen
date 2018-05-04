from graphviz import Digraph
import pygal

def show_graph(graph, filename=None):
    dot = Digraph(comment='zaigen graph')
    for node in graph.nodes:
        if 'inter' in node.name:
            label = '.'
        else:
            node_label = node.name.replace('_', '\n')
            label = f'{node_label} = {node.value:.0f}'
        dot.node(node.name, label)
    for edge in graph.edges:
        dot.edge(edge.start_node.name,
                    edge.end_node.name,
                    label=f'{edge.name} = {edge.weight.value:.0f}')

    dot.format = 'png'
    if filename:
        dot.render(filename=filename, view=False, cleanup=True)
    else:
        dot.view(cleanup=True)

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
