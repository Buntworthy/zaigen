from .context import zaigen

def test_pension():
	g = zaigen.Graph()

	zaigen.helpers.add_salary(g, 1000)
	zaigen.helpers.add_pension(g, 0.05, 0.02)
	zaigen.helpers.add_tax(g, 0.3)
	zaigen.helpers.add_expense(g, 100)
	for _ in range(10):
		g.update()
	zaigen.viz.show_graph(g) 