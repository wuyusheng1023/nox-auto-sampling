import os
from time import sleep
from datetime import datetime
import json

import pytest

import redis
try:
  host = 'redis' if os.environ['DEPLOYMENT'] == 'true' else 'localhost'
except KeyError:
  host = 'localhost'

from interfaces.mock_data import NOX_ANALYZER
from interfaces.nox_analyzer import NOxAnalyzer
from interfaces.helpers import get_random_coef, set_init_mock_redis, pop_expired_redis


class TestGetRandomCoef():

  def test_get_random_coef_returns_a_number(self):
    assert type(get_random_coef()) is float
  
  def test_get_random_coef_with_in_the_range(self):
    assert all([0.9925 <= get_random_coef() <= 1.0075 for i in range(100)])

  def test_get_random_coef_gives_diff_values_each_time(self):
    assert get_random_coef() != get_random_coef()


class TestRedis():

  def test_redis_server_is_on(self):
    r = redis.Redis(host=host, port=6379, db=0)
    r.set('foo', 'bar')  # True
    assert r.get('foo') == b'bar'

  def test_set_init_mock_redis(self):
    r = redis.Redis(host=host, port=6379, db=0)
    r.delete('status')
    set_init_mock_redis()
    v = r.get('status').decode('utf-8')
    assert v == '0'

  def test_pop_expired_items_from_redis_list(self):
    r = redis.Redis(host=host, port=6379, db=0)
    r.delete('data')
    for i in range(10):
      r.lpush('data', i)
    pop_expired_redis(r, 5)
    assert r.llen('data') <= 5


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

  def test_push_given_data_to_redis(self):
    r = redis.Redis(host=host, port=6379, db=0)
    nox = NOxAnalyzer(NOX_ANALYZER)
    while r.rpop('data'):
      r.rpop('data')
    nox.push_mock_data_to_redis(data='111')
    nox.push_mock_data_to_redis(data='222')
    sleep(0.1)
    x_1 = r.rpop('data').decode('utf-8')
    x_2 = r.rpop('data').decode('utf-8')
    assert x_1 == '111'
    assert x_2 == '222'

  def test_parse_data_from_redis(self):
    r = redis.Redis(host=host, port=6379, db=0)
    params = NOX_ANALYZER
    params['datetime'] = str(datetime.utcnow())
    data = {'data': 'NOx analyzer', 'params': params}
    r.lpush('data', json.dumps(data))
    sleep(0.1)
    data = json.loads(r.rpop('data').decode('utf-8'))
    assert 'data' in data.keys()
    assert data['data'] == 'NOx analyzer'
    assert all([x in data['params'].keys() for x in NOX_ANALYZER.keys()])

  def test_push_nox_mock_data_to_redis(self):
    r = redis.Redis(host=host, port=6379, db=0)
    nox = NOxAnalyzer(NOX_ANALYZER)
    while r.rpop('data'):
      r.rpop('data')
    nox.push_mock_data_to_redis()
    sleep(0.1)
    data = json.loads(r.rpop('data').decode('utf-8'))
    assert 'data' in data.keys()
    assert data['data'] == 'NOx analyzer'
    assert all([x in data['params'].keys() for x in NOX_ANALYZER.keys()])
