# 14. 기초 - 1차원 배열
'''[94] 이상한 출석 번호 부르기2
출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

입력
첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

10
10 4 2 3 6 6 7 9 8 5

출력
출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.

5 8 9 7 6 6 3 2 4 10'''
n = int(input())
call = list(map(int, input().split()))
call.reverse() # 리스트의 메소드, call 뒤집기
print(call)    # 리스트 형태 말고 공백으로 구분해서  출력