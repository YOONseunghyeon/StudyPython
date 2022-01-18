# 무한루프
val = 0
print('회원정보프로그램')
while True:
    print('''작업할 번호를 입력하세요.\n1. 회원입력\n2. 회원검색\n3. 회원수정\n4. 회원삭제\n            5. 종료
            숫자입력 : ''', end = '')

    val = int(input())    # 입력

    if val == 1:
        print('회원정보입력 합니다')
        #
    elif val == 2:
        print('회원검색화면으로 전환')
        
    elif val == 3:
        print('회원수정화면으로 전환')
        
    elif val == 4:
        print('회원삭제화면으로 전환')
        
    elif val == 5:
        break
    else:
        print('1~5사이의 수를 입력하세요.')
        continue
print('회원정보프로그램 종료')
