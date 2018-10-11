# 초보자를 위한 파이썬 200제 (016~)

# 018
c1 = 1 + 7j # 복소수형 타입
print(c1.real) # 복소수형에서 실수부만 가져올 경우 real을 사용
print(c1.imag) # 복소수형에서 허수부만 가져올 경우 imag를 사용

c2 = complex(2,3)
print(c2) # complex는 복소수형 상수를 구성가능

# 019
a=1
b=3
ret = a+b

print('a와 b를 더한겂은', end='') # end=''를 사용하는 이유는 줄바꿈 문자를 제거하기 위해서다.
print(ret, end='')
print(' 입니다.')

# 026~033
# 시퀀스 자료형(문자열, 리스트, 튜플)은 객체가 순서를 가지고 나열된다.
# 이러한 시퀀스 자료형은 인덱싱, 슬라이싱, 연결, 반복 등이 가능하다. (+, *, in, len()등..)

strdata = "Time is money!"
listdata = [1,2,[1,2,3]]

print(strdata[5])
print(strdata[-2])
print(listdata[-1])
print(listdata[2][-1])

print(strdata[1:5])
print(strdata[:7])
print(strdata[9:])
print(strdata[:-3])
print(strdata[-3:])
print(strdata[:])
print(strdata[::2])

strdata1 = 'I love python'
strdata2 = '나는 파이썬을 사랑합니다'
listdata1 = ['a','b','c',strdata1, strdata2]
print(len(listdata1[3]))

# 034
txt1 = '자바'
txt2 = '파이썬'
num1 = 5
num2 = 10
print('나는 %s보다 %s에 익숙합니다' %(txt1, txt2)) # %s는 문자열에 대응된다.
print('%s은 %s보다 %d배 더 쉽습니다.' %(txt2,txt1,num1)) # %d는 정수에 대응된다.
print('%d + %d = %d' %(num1,num2,num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%%포인트 증가했다' %num1)
# 이외에도 %c는 문자나 기호 한개에 대응되고 %f는 실수에 대응된다.
