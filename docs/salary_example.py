from context import zaigen

graph = zaigen.Graph()
zaigen.helpers.add_salary(graph, 'my_salary', 10000)
zaigen.viz.show_graph(graph, 'docs/salary_example')
