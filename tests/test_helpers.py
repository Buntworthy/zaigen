from .context import zaigen

def test_pension():
    g = zaigen.Graph()

    salary_weight = zaigen.weights.Constant(100000)
    salary_weight.schedule = zaigen.schedules.CompositeSchedule(
                        zaigen.schedules.Rate(5*[1.02] + 5*[1.01] + 10*[1]),
                        zaigen.schedules.Rate(1.02))
    zaigen.helpers.add_salary(g, 'j_salary', salary_weight)
    zaigen.helpers.add_pension(g, 'bob', 0.06, 'j_salary', 0.05, 0.02)
