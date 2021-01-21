import numpy as np
import redis


def get_random_coef():
  x = np.random.normal(1, 0.0025)
  x = 1.0075 if x > 1.0075 else x
  x = 0.9925 if x < 0.9925 else x
  return x


def set_init_mock_redis():
  r = redis.Redis(host='localhost', port=6379, db=0)
  r.set('status', '0')


# TODO
# - read Redis data
# - if Redis list is too big, pop old items
# - read system time exactly