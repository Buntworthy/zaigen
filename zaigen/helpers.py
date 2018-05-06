import zaigen
from zaigen import schedules

def make_inflation(rate):
    inflation_schedule = schedules.Rate(rate)

    def inflation(schedule):
        if schedule:
            return schedules.CompositeSchedule(schedule, inflation_schedule)
        else:
            return inflation_schedule

    return inflation

def join_graphs(graph1, graph2):
    node1 = graph1.current_node
    node2 = graph2.current_node
    new_node = zaigen.Node('inter')

    for node in graph2.nodes:
        graph1.add_node(node)

    for edge in graph2.edges:
        graph1.add_edge(edge)

    graph1.add_node(new_node)
    graph1.add_edge(zaigen.Edge('transfer',
                    node1,
                    new_node,
                    zaigen.weights.Fraction(1)))
    graph1.add_edge(zaigen.Edge('transfer',
                    node2,
                    new_node,
                    zaigen.weights.Fraction(1)))
    graph1.current_node = new_node


def add_salary(graph, name, amount, inflation=None, increase=None):
    in_node = zaigen.Node('in', node_type='source')
    inter_node = zaigen.Node('inter')
    graph.add_node(in_node)
    graph.add_node(inter_node)
    edge = zaigen.Edge(name,
                        in_node,
                        inter_node,
                        amount)
    if increase:
        increase = schedules.Rate(increase)
    if inflation:
        increase = inflation(increase)

    edge.weight.schedule = increase
    graph.add_edge(edge)
    graph.current_node = inter_node

def add_pension(graph,
                name,
                employee_contribution,
                salary_edge,
                employer_contribution,
                interest_rate):
    pension_pot = zaigen.Node(name + '_pension_pot', node_type='asset')
    interest_in_node = zaigen.Node(name + '_pension_growth', node_type='source')
    pension_contrib_node = zaigen.Node(name + '_pension_contrib', node_type='source')

    graph.add_node(pension_pot)
    graph.add_node(interest_in_node)
    graph.add_node(pension_contrib_node)
    # Make sure to add the edges in the right order
    graph.add_edge(zaigen.Edge(name + '_pension_payment',
                                graph.current_node,
                                pension_pot,
                                zaigen.weights.Fraction(employee_contribution)))
    graph.add_edge(zaigen.Edge(name + '_pension_interest',
                                interest_in_node,
                                pension_pot,
                                zaigen.weights.Interest(interest_rate)))
    graph.add_edge(zaigen.Edge(name + '_pension_contrib',
                                pension_contrib_node,
                                pension_pot,
                                zaigen.weights.EdgeLinked(employer_contribution,
                                    graph.get_edge(salary_edge))))
    add_transfer(graph)

def add_transfer(graph):
    new_end_node = zaigen.Node('inter')
    graph.add_node(new_end_node)
    graph.add_edge(zaigen.Edge('transfer',
                                graph.current_node,
                                new_end_node,
                                zaigen.weights.Fraction(1)))
    graph.current_node = new_end_node

def add_final_savings(graph):
    new_end_node = zaigen.Node('savings', node_type='asset')
    graph.add_node(new_end_node)
    graph.add_edge(zaigen.Edge('transfer',
                                graph.current_node,
                                new_end_node,
                                zaigen.weights.Fraction(1)))
    graph.current_node = new_end_node

    interest_in_node = zaigen.Node('interest_in', node_type='source')
    graph.add_node(interest_in_node)

    graph.add_edge(zaigen.Edge('saving_growth',
                    interest_in_node,
                    new_end_node,
                    zaigen.weights.Interest(0.01)))


def add_expense(graph, name, value, schedule):
    expense_out = zaigen.Node(name + '_expense_out', node_type='sink')

    weight = zaigen.weights.Constant(value)
    weight.schedule = schedule

    graph.add_node(expense_out)
    graph.add_edge(zaigen.Edge(name + '_expense',
                                graph.current_node,
                                expense_out,
                                weight))
    add_transfer(graph)

def add_mortgage(graph, principal, term, rate):
    mortgage = zaigen.Node('mortgage')
    mortgage.value = -principal
    mortgage_interest_payments = zaigen.Node('mortgage_interest', node_type='sink')
    mortgage_repayment = zaigen.weights.Constant(
        zaigen.util.calculate_mortage_repayment(principal, term, rate))
    mortgage_interest = zaigen.weights.Interest(rate)

    graph.add_node(mortgage)
    graph.add_node(mortgage_interest_payments)
    graph.add_edge(zaigen.Edge('mortgage_repayments',
                    graph.current_node,
                    mortgage,
                    mortgage_repayment))
    graph.add_edge(zaigen.Edge('mortgage_interest',
                    mortgage_interest_payments,
                    mortgage,
                    mortgage_interest))

    add_transfer(graph)

def add_tax(graph, rate):
    tax_out = zaigen.Node('tax_out', node_type='sink')

    graph.add_node(tax_out)
    graph.add_edge(zaigen.Edge('tax',
                                graph.current_node,
                                tax_out,
                                zaigen.weights.Fraction(rate)))
    add_transfer(graph)
