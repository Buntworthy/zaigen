from .context import zaigen

def test_schedule():
	value = 10
	s = zaigen.schedules.Schedule()
	out_value = s.update(value)
	assert out_value == value

def test_constant_rate():
	value = 10
	rate = 0.5
	s = zaigen.schedules.ConstantRate(rate)
	out_value = s.update(value)
	assert out_value == value*rate

def test_piecewise_rate():
	value = 10
	rate = 2*[2] + 5*[1.5]
	s = zaigen.schedules.PiecewiseRate(rate)
	out_value = s.update(value)
	out_value = s.update(out_value)
	out_value = s.update(out_value)
	assert out_value == value*rate[0]*rate[1]*rate[2]

def test_composite_schedule():
	value = 10
	rate1 = 0.5
	rate2 = 2*[2] + 5*[1.5]
	s1 = zaigen.schedules.ConstantRate(rate1)
	s2 = zaigen.schedules.PiecewiseRate(rate2)
	s = zaigen.schedules.CompositeSchedule(s1, s2)

	out_value = s.update(value)
	out_value = s.update(out_value)

	assert out_value == rate2[1]*rate1*rate2[0]*rate1*value
