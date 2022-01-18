# if구문 - 흐름제어
#name = '길동'
name = ('승현', '태경', '기영', '광조', '다원')

# if name == '승현' or name =='태경':
if '승현' in name:
    print('의사를 만나러 갑니다.')  #print 줄이 맞아야함(중요!)
    print('의사쌤한테 인사합니다.')
elif name == '다윈' : 
    print('주사실로갑니다.')    
else:
    print('호출할때까지 대기합니다.')

x = 2
if x!= 10:
    pass
else:
    pass