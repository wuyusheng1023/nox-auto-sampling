import redis
import json
import time
from datetime import datetime

while True:
  r = redis.Redis(host='localhost', port=6379, db=0)
  list_len = r.llen('data')

  if list_len == 0:
    print(f'{datetime.now()}: The list is empty\n')
  else:
    print(f'{datetime.now()}: The list length: {list_len}')
    item = json.loads(r.rpop('data').decode('utf-8'))
    print(f'Pop one item:\n{item}\n')
  
  time.sleep(2)
