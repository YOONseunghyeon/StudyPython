# 기본 for문
# arr = list(range(1, 100))
# for i in arr:
#     print(f'{i:2.1f}')

#튜플로 for 문
# arr2 = ('me', 'my', 'friend','jane')

# #f는 format string
# for item in arr2:
#     print(f'{item:>10}')

# # 합계 for문
# numbers = list(range(1,21,2))  #1~10가지
# print(numbers)
# res = 0
# for item in numbers:
#     res += item

# print(f'{numbers[-1]} 까지의 총 합은 {res}입니다.')

# # 홀수짝수 구분
# numbers = list(range(1, 21))

# for item in numbers:
#     if item % 2 == 0:  #짝수
#         print(f'{item}은 짝수')

# 15 제외하고 추출
#numbers = list(range(1, 21))

# for item in numbers:
#     if item == 15:
#         continue  # 15를 만나면 다시 위로감 (해당 조건을 제외하고)

#     if item % 2 == 1:  #if item % 2 != 0
#          print(f'{item}은 홀수')

# 구구단
# #print('구구단 프로그램')
# for i in range(2, 10):   #2단 ~ 9단까지 
#     if i ==8:
#         continue
#     #print(f'{i}단 시작')
#     for j in range(1, 10): #1 ~ 9
#         print(f'{i} x {j} = {i*j:2d}', end='  ') #2d는 결과값 칸맞추는거 4,6,8,10,12
#     print('') # print() 해도 값같음

# inline for문
# a = [1, 2, 3, 4]
# result = [i * 3 for i in a]
# print(result)
# #기존 for 문
# t = []
# for i in a:
#     t.append(i * 3)

# print(t)
