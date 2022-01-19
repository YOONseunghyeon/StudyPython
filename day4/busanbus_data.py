#부산버스 노선별 이용건수
import csv   #csv는 표준 라이브러리

file_name = '부산버스정보.csv'   #csv는 파일 데이터
f = open('부산버스정보.csv', mode = 'r' , encoding='utf-8')

reader = csv.reader(f, delimiter=',')
next(reader)  #첫줄을 없애줌 = 헤더를 없애는 역할
for line in reader:
    print(line)

f.close()