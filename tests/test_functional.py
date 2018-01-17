from .context import zaigen

import pytest

def test_simple_transfers():
	"""
	in1 --> inter1 --> inter2 --> saving1
			  |    		 |
			  v			 v
	in2 --> saving2		out1
	"""

	g = zaigen.Graph()
	g.add_node(zaigen.Node('in1'))
	g.add_node(zaigen.Node('in2'))
	g.add_node(zaigen.Node('inter1'))
	g.add_node(zaigen.Node('inter2'))
	g.add_node(zaigen.Node('saving1'))
	g.add_node(zaigen.Node('saving2'))
	g.add_node(zaigen.Node('out1'))

	g.add_edge(zaigen.Edge('income1', 
				start_node=g.get_node('in1'), 
				end_node=g.get_node('inter1'), 
				weight=100)) # constant transfer
	g.add_edge(zaigen.Edge('save1', 
				start_node=g.get_node('inter1'), 
				end_node=g.get_node('saving2'), 
				weight=10)) # constant transfer
	g.add_edge(zaigen.Edge('interest1', 
				start_node=g.get_node('in2'), 
				end_node=g.get_node('saving2'), 
				weight=zaigen.weights.Interest(0.1))) # 10% interest
	g.add_edge(zaigen.Edge('remain1', 
				start_node=g.get_node('inter1'), 
				end_node=g.get_node('inter2'), 
				weight=zaigen.weights.Remaining(1))) # all remaining
	g.add_edge(zaigen.Edge('expense1', 
				start_node=g.get_node('inter2'), 
				end_node=g.get_node('out1'), 
				weight=50)) # constant transfer
	g.add_edge(zaigen.Edge('remain2', 
				start_node=g.get_node('inter2'), 
				end_node=g.get_node('saving1'), 
				weight=zaigen.weights.Remaining(1))) # all remaining

	for _ in range(10):
		n = g.get_node('saving2')
		print(n.value)
		g.update()

	assert g.get_node('in1').value == -1000
	assert g.get_node('inter1').value == 0
	assert g.get_node('inter2').value == 0
	assert g.get_node('saving2').value == pytest.approx(159.37, 0.01)