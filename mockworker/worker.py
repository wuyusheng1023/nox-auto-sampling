from copy import copy

import numpy as np
import redis

from .data import NOX_ANALYZER, MFC_SETPOINT, UPS


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

  def _get_raw_data(self):
    self.data['NO'] *= get_random_coef()
    self.data['NOx'] *= get_random_coef()
