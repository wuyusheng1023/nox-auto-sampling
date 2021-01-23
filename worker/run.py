import os
from time import sleep

import redis
try:
  host = 'redis' if os.environ['DEPLOYMENT'] == 'true' else 'localhost'
except KeyError:
  host = 'localhost'

from interfaces.helpers import set_init_mock_redis, pop_expired_redis
from interfaces.helpers import TimeChecker
from interfaces.nox_analyzer import NOxAnalyzer


def mock_worker():
  r = redis.Redis(host=host, port=6379, db=0)
  set_init_mock_redis()
  nox = NOxAnalyzer(r)
  time_checker_1 = TimeChecker(1)

  while True:
    if time_checker_1.detect_alarm():
      pop_expired_redis(r, 100)
      log = nox.push_mock_data_to_redis()
      time_checker_1.alarm = False
      print(log)
      sleep(0.1)


if __name__ == '__main__':
  mock_worker()
