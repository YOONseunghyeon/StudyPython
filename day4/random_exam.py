# Random 함수
from random import * #패키지를 불러오는 거 = import

#print(random.choice(range(1, 7)))   #주사위 (시작숫자,마지막숫자+1)

# lottery (우리나라 로또lotto)
numbers = list(range(1, 46))  #1~45
lottery = [] # list()

for i in range(6):
    lottery.append(choice(numbers))

print(lottery)  # 이때는 중복이 나올수 있다
#같은수가 나오면 다시 그 수 랜덤 추출 
#현재 완전한 로또 프로그램은 파이썬에 없음.