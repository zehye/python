scope = [1,2,3]
for x in scope:
    print(x)
#     #break
else:
    print('perfect!')

x=0
while x < 10:
    x=x+1
    if x < 3:
        continue
    print(x)
    if x > 7:
        break


x = 1
total = 0
while 1: # 1은 참일때, 0은 거짓일때를 의미 (좀 더 엄밀히 0이 아닌값은 참, 0인값은 거짓)
    total = total + x
    if total > 100000:
        print(x)
        print(total)
        break
    x = x+1
