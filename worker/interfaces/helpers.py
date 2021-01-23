import os
import random
from datetime import datetime
import math

import redis
try:
  host = 'redis' if os.environ['DEPLOYMENT'] == 'true' else 'localhost'
except KeyError:
  host = 'localhost'


def get_random_coef():
  x = random.gauss(1, 0.0025)
  x = 1.0075 if x > 1.0075 else x
  x = 0.9925 if x < 0.9925 else x
  return x


def set_init_mock_redis():
  r = redis.Redis(host=host, port=6379, db=0)
  r.set('status', '0')


def pop_expired_redis(r, list_len=1000):
  while r.llen('data') > list_len:
    r.rpop('data')


class TimeChecker():
  def __init__(self, interval=1):
    self._interval = max([1, math.floor(interval)])
    self._t_prev = datetime.now()

  def detect_alarm(self):
    now = datetime.now()
    print(now)
    print(self._t_prev)
    print("---------------------")
    if math.floor(now.timestamp()) - math.floor(self._t_prev.timestamp()) >= self._interval:
      self._t_prev = now
      return True
    else:
      return False
