# 별 찍기 - 16

n = int(input())

for i in range(1, n+1):
    print(' ' * (n-i), end='')
    for j in range(i):
        print('*', end=' ')
    print()
