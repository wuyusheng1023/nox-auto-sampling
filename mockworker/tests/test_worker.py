from ..data import NOX_ANALYZER
from ..worker import NOxAnalyzer


class TestNOxAnalyzer():

  def test_get_raw_data(self):
    pass
    nox = NOxAnalyzer()
    assert nox._get_raw_data()
  
