from ..data import NOX_ANALYZER
from ..worker import get_random_coef, NOxAnalyzer


class TestGetRandomCoef():

  def test_get_random_coef_returns_a_number(self):
    assert type(get_random_coef()) is float
  
  def test_get_random_coef_with_in_the_range(self):
    assert all([0.9925 <= get_random_coef() <= 1.0075 for i in range(100)])


class TestNOxAnalyzer():

  def test_class_init_properly_with_mock_data(self):
    nox = NOxAnalyzer(NOX_ANALYZER)
    assert nox.data == NOX_ANALYZER

  def test_get_raw_data(self):
    nox = NOxAnalyzer(NOX_ANALYZER)
    nox._get_raw_data()
    assert nox.data
  
