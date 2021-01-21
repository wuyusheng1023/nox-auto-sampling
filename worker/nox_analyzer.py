from copy import copy
from datetime import datetime
import json

import redis

from .mock_data import NOX_ANALYZER
from .helpers import get_random_coef


class NOxAnalyzer():

  def __init__(self, data=None, status='0'):
    self.data = copy(NOX_ANALYZER)
    self.status = status
    self.r = redis.Redis(host='localhost', port=6379, db=0)

  def _get_mock_raw_data(self, set_points):
    prev_no = self.data['NO']
    diff_no = set_points['NO'] - prev_no
    self.data['NO'] = prev_no*get_random_coef() + diff_no*0.2
    prev_nox = self.data['NOx']
    diff_nox = set_points['NOx'] - prev_nox
    self.data['NOx'] = prev_nox*get_random_coef() + diff_no*0.2
    return self.data

  def push_mock_data_to_redis(self, data=None):
    if data:
      self.r.lpush('data', data)
    else:
      if self.status == '0':
        set_points = {'NO': NOX_ANALYZER['NO'], 'NOx': NOX_ANALYZER['NOx']}
      elif self.status == '1':
        # TODO
        pass
      params = self._get_mock_raw_data(set_points)
      params['datetime'] = str(datetime.utcnow())
      data = {'data': 'NOx analyzer', 'params': params}
      self.r.lpush('data', json.dumps(data))
