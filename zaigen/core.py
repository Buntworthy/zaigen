import zaigen

class Graph(object):
    """Graph data structure for outlining the flow of money in the simulation.
    """

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.current_node = None

    def add_node(self, node):
        while node.name in [node.name for node in self.nodes]:
            node.name += '.'

        # TODO check for duplication
        if not self.nodes:
            self.current_node = node
        self.nodes.append(node)

    def get_node(self, node_name):
        matching_nodes = [node for node in self.nodes if node.name == node_name]
        return matching_nodes[0]

    def add_edge(self, edge):
        while edge.name in [edge.name for edge in self.edges]:
            edge.name += '.'
        self.edges.append(edge)

        if edge.start_node not in self.nodes:
            self.add_node(edge.start_node)
        if edge.end_node not in self.nodes:
            self.add_node(edge.end_node)

    def get_edge(self, edge_name):
        matching_edges = [edge for edge in self.edges if edge.name == edge_name]
        return matching_edges[0]

    def update(self):
        self.reset()
        self.update_pre_edges()
        self.main_update()
        self.record()

    def record(self):
        for node in self.nodes:
            node.record()
        for edge in self.edges:
            edge.record()

    def reset(self):
        for node in self.nodes:
            node.reset()
        for edge in self.edges:
            edge.reset()

    def main_update(self):
        # Breadth first update
        while not self.updated:
            nodes_to_update = [node
                for node in self.nodes
                    if node.current_in_degree==0
                    and not node.updated]
            #import pdb; pdb.set_trace()
            for node in nodes_to_update:
                node.update()

    def update_pre_edges(self):
        pre_update_edges = (edge for edge in self.edges if edge.pre_update)
        for edge in pre_update_edges:
            edge.update()

    @property
    def updated(self):
        if (all((node.updated for node in self.nodes)) and
            all((edge.updated for edge in self.edges))):
            return True
        else:
            return False

    def __str__(self):
        info_string = 'Zaigen graph\n'
        info_string += '\tNodes:\n'
        for node in self.nodes:
            node_string = node.__repr__()
            info_string += '\t\t' + node_string + '\n'
        info_string += '\tEdges:\n'
        for edge in self.edges:
            edge_string = edge.__repr__()
            info_string += '\t\t' + edge_string + '\n'
        return info_string

class Node(object):
    """Basic node data structure for money graph"""

    def __init__(self, name, node_type=None):
        self.name = name
        self.upstream_nodes = []
        self.downstream_nodes = []
        self.edge_list = []
        self.value = 0
        self.updated = False
        self.current_in_degree = self.in_degree
        self.history = []
        self.type = node_type

    def update(self):
        print(f'Updating Node: {self.name}')
        for node in self.downstream_nodes:
            print(node)
            for edge in node.edge_list:
                if edge.start_node is self and not edge.updated:
                    edge.update()
            node.current_in_degree -= 1
        self.updated = True

    def record(self):
        self.history.append(self.value)

    def reset(self):
        self.updated = False
        self.current_in_degree = self.in_degree

    @property
    def in_degree(self):
        return len(self.upstream_nodes)

    def __repr__(self):
        return f'Node(name=\'{self.name}\')'

class Edge(object):
    """Basic edge data structure for money graph"""

    def __init__(self, name, start_node, end_node, weight):
        self.name = name
        self.start_node = start_node
        self.end_node = end_node
        self.updated = False
        self.applied = False
        if isinstance(weight, (int, float)):
            self.weight = zaigen.weights.Constant(weight)
        else:
            self.weight = weight
        self.history = []
        self.start_node.edge_list.append(self)
        self.end_node.edge_list.append(self)
        self.start_node.downstream_nodes.append(self.end_node)
        self.end_node.upstream_nodes.append(self.start_node)

    def update(self):
        print(f'Updating Edge: {self.name}')
        self.weight.update(self)
        self.start_node.value -= self.weight.value
        self.end_node.value += self.weight.value
        self.updated = True

    def record(self):
        self.history.append(self.weight.value)

    def reset(self):
        self.updated = False

    @property
    def pre_update(self):
        return self.weight.pre_update

    def __repr__(self):
        return f'Edge(name=\'{self.name}\', ' \
                        f'start_node=\'{self.start_node.name}\', ' \
                        f'end_node=\'{self.end_node.name}\', ' \
                        f'weight={self.weight})'
