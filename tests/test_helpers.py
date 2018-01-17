from .context import zaigen

def test_pension():
	g = zaigen.Graph()

	zaigen.helpers.add_salary(g, 100)

	zaigen.helpers.add_pension(g, 0.05, 0.02)
	zaigen.viz.show_graph(g) 