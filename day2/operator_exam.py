# 연산자 - 사칙연산
a = 11
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)     # 몫
print(a % b)      # 나머지

# 문자열 연산
stat1 = 'Hello'
stat2 = 'Wolrd'
res = stat1 + stat2
print(res)   # 문자를 합친거
print(stat1,stat2)   # 같이 출력만 해줌 (합친거 아님)
# print(stat1 - stat2)   # 문자열엔 빼기 없음
print(stat1 *5)
#print(stat1 *stat2) # 문자열 변수끼리의 곱은 없음
#print(stat1 /3) # 문자열 나누기 없음 

# 문자열 길이
print(len(stat1))
stat3= '안녕하세요'
print(len(stat3))

# 문자열 인덱스, 리스트와 동일한 작업
# print(stat3[0])   #stat3의 0번째 값 알려줘
# print(stat3[1])   
# print(stat3[2])   
# print(stat3[3])   
# print(stat3[4])  
# print(stat3[5])   #예외발생 모든인덱스은 0번부터시작

#stat3[0] = '저'
#stat3[1] = '리'
#print(stat3)

print(stat3[-1])
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])
print(stat3[-5])

# 문자열 자르기
일시 = '2022-01-17 14:39:25'

print(일시[:4],'년')
print(일시[5:7],'월')
print(일시[8:10],'일')
print(일시[11:13],'시')
print(일시[14:16],'분')
print(일시[17:],'초')    # 맨앞과 맨뒤는 생략가능

print(일시[-5:-3],'분')

list_a = [1,2,3,4,5]
list_a[1]= 19
print(list_a)

print(stat3)       #stat3 = '안녕하세요'
stat4 = '저리가' + stat3[3:]
print(stat4)

##문자열포맷팅
첫번째 = '투'
두번째 = '유'
str1 = "I'm so happy {0} U. are {1}" . format(첫번째,두번째)
print(str1)   #{0} = 첫번째   {1} = 두번째

str2 = f"I'm so happy {첫번째} U. are {두번째}?"
print(str2)  # 최신 포맷팅법 

money = 10000000000000
print(format(money, ',d'))

#현재일시 생성및 현재 시간 변경
from datetime import datetime
now = datetime.now()   #현재일시 생성
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))

#숫자 소숫점뒤자리 
import math
myPi = math.pi
print(myPi)


print('{0}'.format(myPi))
print('{0:0.6f}'.format(myPi))
print(f'{myPi:0.6f}')

full_name = 'YOONseunghyeon'
age = 25
greeting = '''안녕하세요. 저는 {0}입니다,
나이는 {1}살 이구요.'''.format(full_name, age)
greeting = f'''안녕하세여요. 저는 {full_name}입니다.
나이는 {age:0.1f}살 이구요.'''

print(greeting)

part_name = full_name.split()  
#split 뒤에 아무것도 안넣으면 스페이스로 짤라냄
print(type(part_name))
print(part_name)


# | split
code = 'TEST|2022|01|17|F45678'
split_codes = code.split('|')
print(split_codes)
#full_name = 'YOON seunghyeon'
print(full_name . replace('YOON ' , 'Ashley'))
full_name.replace('YOON', 'Ashley')
  #strip == Oracle TRIM과 동일
aaa = '        Hello, world       '
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.strip())

print(full_name.index('Y'))   #0    #full_name = 'YOONseunghyeon'
print(full_name.index('O'))   #1
print(full_name.index('N'))   #2
print(full_name.index('s'))   #4 
print(full_name.index('e'))   #5
print(full_name.index('g'))   #8

print(full_name.find('X'))   #FIND로 찾아서 -1이 나온다면 full_name에 없다는소리
print(full_name.find('OO')) #1

print('-'.join(full_name))  #사이에 -넣기

print(full_name.upper())   #모두 대문자로
print(full_name.lower())   #모두 소문자로









