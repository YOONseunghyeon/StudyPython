# 함수 선언 및 사용

# 더하기 함수 선언
from audioop import mul


def add(a, b):
    res = a + b

    return res   #값을 반환 해준 add(a3, b4) ->mid_val 에 할당

# 함수 사용
print(add(24786, 4324))

mid_val = add(3, 4)
print(mid_val * 3)

print(add(6))

# 함수종류
#매개변수(입력값)이 없는 형태
def say_Hello():
    return 'Hello~'

print(say_Hello())
print(say_Hello(), 'my friend')

val = say_Hello()
print(val.replace('o~',''))

# 결과값이 없는 형태
def say_hello(name):
    print(f'Hello~{name}')
    #return None

say_hello('승현')

 # 둘다없는 경우
def say_goodbye():
    print('Bye bye~')

say_goodbye()

# 매개변수 지정
def multi(a, b):
    return a * b

print(multi(2,9))
print(multi(8,9))

# 배겨변수가 개수가 가변적일때
def plus(*args):
    res = 0
    
    for i in args:
        res += i

    return res

print(plus(1))
print(plus(1,2,3))
print(plus(1,2,3,4,5,6,7,8,9,10))


# 리턴값이 두개이상
def mul_and_div(x ,y):
    mul= x * y
    div= x / y

    return (mul, div)  #튜플

(res1, res2) = mul_and_div(7, 8)
print(res1,res2)

def 사칙연산(x, y):
    return (x+y, x-y, x*y, x/y)

res1, res2, res3, res4 = 사칙연산(9,5)
print(type(사칙연산(1, 2)))