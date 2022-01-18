# 변수 라이프스코프
a = 1     #0
res = 0   #상관없는 애 , 변수 지정때매 먼저 쓴거일뿐 결과론적으로 필요없음

def vartest(a):   #2    5~7열은 함수 선언문
    a = a + 1     #3
    return a      #4

a = vartest(a)    #1    #입력값에 1을 더헤 리턴해주는 함수  사용은 9번열에서
print(res)          #5    

#변수 라이프 스코프 2
a = 10                       # 전역변수-13절,19열,20열            

def vartest(a):              # 지역변수-15열,16열,17열
    a = a + 1
    return a

res = vartest(a)
print(a)






