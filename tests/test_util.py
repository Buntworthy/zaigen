from .context import zaigen
import pytest

def test_mortgage_repayments():
    # Wikipedia example https://en.wikipedia.org/wiki/Mortgage_calculator
    repayment = zaigen.util.calculate_mortage_repayment(200000, 30, (6.5/100))
    assert repayment == pytest.approx(12*1264.14, rel=1e-4)
