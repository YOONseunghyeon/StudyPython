# 리스트 연산
from pickle import TUPLE1


arr = list(range(5)) #0부터4까지임 0이 시작점
print(arr)

arr = list(range(1, 6)) #1부터
print(arr)

arr = list(range(2, 101, 2)) #(시작숫자, 원하는숫자+1,얼마나증감하는가)
print(arr)

print(arr[0] + arr[5])

#2차원 배열 (리스트)
arr2 = [1, 2, ['Hi', 'My', 'Friend']]
print(arr2[0])
print(arr2[2])
print(arr2[2][1])
print(arr2[2][1][0]) #['Hi', 'My', 'Friend'] -> 'My'-> M


arr3 = list(range(1, 4))
print(arr3)
print(arr3 * 3)
print(arr3 + 3)
print(len(arr))  #arr = list(range(2, 101, 2))

# 리스트     #arr3 = list(range(1, 4))
print('--리스트 내장함수')
del(arr3[1])
print(arr3)  # 1,3

arr3.remove(1)  #index 지우지말고 숫자1을 지워라 
print(arr3)

# 리스트 삭제
arr4 =[4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5]
arr4.remove(3)   # 최초의 3만 지우는 remove
print(arr4)
del(arr4[8]) # index를 삭제 8번째 자리 삭제(0~10자리까지있음, 8자리는 3)
print(arr4)

arr4.sort()
print(arr4)  #오름차순

arr4.reverse()
print(arr4)  #내림차순

arr4.insert(2, 10) #0,1,2 자리에 10
print(arr4)

tup1 = tuple(range(1,6))
print(tup1)             #튜플은 함수 없음
print(tup1[3])

#tip1[0 ]= 99
print(tup1)

# 딕셔너리
dic1 = {1 : 'a'}
dic1[2] = 'b'
print(dic1)

dic1['name'] = 'YOON' #리스트는 문자형 숫자형 다써도 된다 [] <-list
print(dic1)

del dic1['name']   # del 제거 'name'
print(dic1)

print(dic1.keys())
print(dic1.values())
print(dic1.items())

# 리스트를 튜플 변환
print('--리스트/튜플 변환')
print(arr4)
tup2 = tuple(arr4) #튜플로 변환
print(tup2)

arr4.sort()

print(tup1)
arr5 = list(tup1)
print(arr5)
arr5.append(6)
print(arr5)
tup1 = tuple(arr5)
print(tup1)