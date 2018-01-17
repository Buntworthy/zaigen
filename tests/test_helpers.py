from .context import zaigen

def test_pension():
	g = zaigen.Graph()

	salary_weight = zaigen.weights.Constant(100000)
	salary_weight.schedule = zaigen.schedules.CompositeSchedule(
						zaigen.schedules.PiecewiseRate(5*[1.02] + 5*[1.01] + 10*[1]),
						zaigen.schedules.ConstantRate(1.02))
	zaigen.helpers.add_salary(g, 'j_salary', salary_weight)
	salary_edge = g.get_edge('j_salary')
	zaigen.helpers.add_pension(g, 0.06, salary_edge, 0.05, 0.02)
	zaigen.helpers.add_tax(g, 0.3)
	zaigen.helpers.add_expense(g, 100)
	for _ in range(20):
		g.update()
	zaigen.viz.show_graph(g) 
	zaigen.viz.plot_node(g.nodes)
	zaigen.viz.plot_edge(g.edges)