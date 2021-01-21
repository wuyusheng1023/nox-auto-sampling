from copy import copy

import numpy as np
import redis

from .mock_data import NOX_ANALYZER, MFC_SETPOINT, UPS


mfc = {'set': MFC_SETPOINT, 'read': 0}
ups = UPS


def get_random_coef():
  x = np.random.normal(1, 0.0025)
  x = 1.0075 if x > 1.0075 else x
  x = 0.9925 if x < 0.9925 else x
  return x


def set_init_mock_redis():
  r = redis.Redis(host='localhost', port=6379, db=0)
  r.set('status', '0')


class NOxAnalyzer():

  def __init__(self, data=None):
    self.data = copy(NOX_ANALYZER)
    self.r = redis.Redis(host='localhost', port=6379, db=0)

  def _get_mock_raw_data(self, set_points):
    prev_no = self.data['NO']
    diff_no = set_points['NO'] - prev_no
    self.data['NO'] = prev_no*get_random_coef() + diff_no*0.2
    prev_nox = self.data['NOx']
    diff_nox = set_points['NOx'] - prev_nox
    self.data['NOx'] = prev_nox*get_random_coef() + diff_no*0.2

  def push_data_to_redis(self, data=None, ttl=60):
    if data:
      self.r.lpush('data', data)
