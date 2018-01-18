from context import zaigen

# Define the nodes and edges
in_node = zaigen.Node('in')
out_node = zaigen.Node('out')
transfer = zaigen.Edge('transfer',
                        in_node,
                        out_node,
                        100)

# Add them to the graph object
g = zaigen.Graph()
g.add_node(in_node)
g.add_node(out_node)
g.add_edge(transfer)
zaigen.viz.show_graph(g, 'docs/simple_graph')