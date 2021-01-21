from time import sleep

from interfaces.helpers import set_init_mock_redis
from interfaces.nox_analyzer import NOxAnalyzer


# def mock_worker():
set_init_mock_redis()
nox = NOxAnalyzer()

while True:
  log = nox.push_mock_data_to_redis()
  print(log)
  sleep(1)


# if __name__ == '__main__':
#   mock_worker()
