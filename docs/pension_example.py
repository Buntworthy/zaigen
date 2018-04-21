from context import zaigen

graph = zaigen.Graph()
zaigen.helpers.add_salary(graph, 'my_salary', 10000)
zaigen.helpers.add_pension(graph, 'alice', 0.04, 'my_salary', 0.05, 0.02)
zaigen.viz.show_graph(graph, 'docs/pension_example')
