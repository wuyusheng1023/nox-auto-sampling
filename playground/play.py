import redis
import json
import time

while True:
  r = redis.Redis(host='localhost', port=6379, db=0)
  try:
    print(json.loads(r.rpop('data').decode('utf-8')))
    print(r.llen('data'))
  except:
    print('Now the list is empty')
    time.sleep(10)
