import zaigen

g = zaigen.Graph()

# make inflation helper function, wrap any schedule in this to add inflation
inflation = zaigen.helpers.make_inflation(1.02)

# Weight is the value of the transfer this changes according to the schedule
salary_weight = zaigen.weights.Constant(53500)
salary_weight.schedule = inflation(
				zaigen.schedules.PiecewiseRate(5*[1.02] + 5*[1.01] + 10*[1]))
# Create the salary
zaigen.helpers.add_salary(g, 'j_salary', salary_weight)
zaigen.helpers.add_pension(g, 'justin', 0.06, 'j_salary', 0.05, 0.02)
zaigen.helpers.add_tax(g, 0.4)

g2 = zaigen.Graph()
zaigen.helpers.add_salary(g2, 'c_salary',
	zaigen.weights.Constant(30500))
zaigen.helpers.add_tax(g2, 0.3)

zaigen.helpers.join_graphs(g, g2)


zaigen.helpers.add_mortgage(g, 170000, 17, 0.0244)


zaigen.helpers.add_expense(g, 42000, (inflation(None)))
zaigen.helpers.add_final_savings(g)
zaigen.viz.show_graph(g)

for i in range(10):
	print(i)
	g.update()

#zaigen.viz.plot_node([node for node in g.nodes if node.type == 'asset'])
zaigen.viz.plot_node(g.nodes)
zaigen.viz.plot_edge(g.edges)
