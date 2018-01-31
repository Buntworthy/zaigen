from context import zaigen

# Create a graph, we also need to add node in order to connect the expense
graph = zaigen.Graph()
graph.add_node(zaigen.Node('in'))

zaigen.helpers.add_expense(graph, 1000, None)
zaigen.helpers.add_expense(graph, 200, None)
zaigen.viz.show_graph(graph, 'docs/expense_example_2')
