from ..data import NOX_ANALYZER
from ..worker import NOxAnalyzer


class TestNOxAnalyzer():

  def test_class_init_properly_with_mock_data(self):
    nox = NOxAnalyzer(NOX_ANALYZER)
    assert nox.data == NOX_ANALYZER

  def test_get_raw_data(self):
    nox = NOxAnalyzer(NOX_ANALYZER)
    nox._get_raw_data()
    assert nox.data
  
