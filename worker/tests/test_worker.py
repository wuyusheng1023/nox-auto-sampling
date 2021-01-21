import redis

from ..data import NOX_ANALYZER
from ..worker import get_random_coef, set_init_mock_redis, NOxAnalyzer


class TestGetRandomCoef():

  def test_get_random_coef_returns_a_number(self):
    assert type(get_random_coef()) is float
  
  def test_get_random_coef_with_in_the_range(self):
    assert all([0.9925 <= get_random_coef() <= 1.0075 for i in range(100)])

  def test_get_random_coef_gives_diff_values_each_time(self):
    assert get_random_coef() != get_random_coef()


class TestRedis():

  def test_redis_server_is_on(self):
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')  # True
    assert r.get('foo') == b'bar'

  def test_set_init_mock_redis(self):
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.delete('status')
    set_init_mock_redis()
    v = r.get('status').decode("utf-8")
    assert v == '0'


class TestNOxAnalyzer():

  def test_class_init_properly_with_mock_data(self):
    nox = NOxAnalyzer(NOX_ANALYZER)
    assert nox.data == NOX_ANALYZER

  def test_get_mock_raw_data_is_nonempty(self):
    nox = NOxAnalyzer(NOX_ANALYZER)
    set_points = {'NO': NOX_ANALYZER['NO'], 'NOx': NOX_ANALYZER['NOx']}
    nox._get_mock_raw_data(set_points)
    assert nox.data
  
  def test_get_mock_raw_data_is_diff_from_previous(self):
    nox = NOxAnalyzer(NOX_ANALYZER)
    set_points = {'NO': NOX_ANALYZER['NO'], 'NOx': NOX_ANALYZER['NOx']}
    nox._get_mock_raw_data(set_points)
    no_1, nox_1 = nox.data['NO'], nox.data['NOx']
    nox._get_mock_raw_data(set_points)
    no_2, nox_2 = nox.data['NO'], nox.data['NOx']
    assert (no_1 != no_2) and (nox_1 != nox_2)
