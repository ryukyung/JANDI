# 4-1. 상하좌우
# 나의 풀이
n = int(input())
mv = input().split()
x, y = 1, 1

for i in mv:
    if x < 1 and y < 1:
        continue
    else:
        if i == 'R':
            y += 1
            print(x, y)
        elif i == 'L':
            y -= 1
            print(x, y)
        elif i == 'U':
            x -= 1
            print(x, y)
        elif i == 'D':
            x += 1
            print(x, y)
# 범위 벗어남을 해결하지 못함

# 해설
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]  # 왼 오 위 아래
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):  # 4번 반복
        if plan == move_types[i]:  # [0]~[3]까지 입력한만큼 반복
            nx = x+dx[i]  # 'D'면 1+1
            ny = y+dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:  # 범위 체크
        continue
    x, y = nx, ny
print(x, y)