# 초보자를 위한 파이썬 200제 (016~)

# 034
# 파이썬에서 시간을 지연시키는 함수
from time import sleep
for i in range(100):
    msg = '\r진행률 %d%%'%(i+1)
    print(''*len(msg), end='')
    print(msg, end='')
    sleep(0.1)
