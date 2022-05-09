'''
[10]
정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자.
'''
i = int(input())    # intput은 기본적으로 문자형으로 저장되므로 int 형변환 필요
print(i)


'''
[11]
문자형(char)으로 변수를 하나 선언하고,
변수에 문자를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.
'''
ch = input()
print(ch)


'''
[12]
실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후 저장되어 있는 실수값을 출력해보자.
'''
fl = float(input())
print(fl)


'''
[13]
정수(int) 2개를 입력받아 그대로 출력해보자. (단, 띄어쓰기를 기준으로 입력한다.)
입력 : 1 5
출력 : 1 5
'''
a = list(map(int, input().split()))
print(a[0], a[1])


'''
[14]
2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.

아스키 코드란?

컴퓨터가 문자를 읽을 수 있도록 문자에 대응하는 숫자들이 존재한다.
예 ) A => 1100001
이때의 문자가 '아스키 문자'이며, 숫자가 '아스키 코드'이다.
'''
a = input().split()
print(a[1], a[0])


'''
[15]
실수(float) 1개를 입력받아 저장한 후,
저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여 소수점 이하 둘 째 자리까지 출력하시오.

Tip::

반올림 함수 round()를 이용하면 된다.
'''
i = round(float(input()), 2)  # 반올림 함수 round(숫자, 소숫점 몇자리까지)
print(i)


'''
[16]
int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자.
'''
a = int(input())
print(a, a, a)


'''
[17]
어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
콜론(:) 기호를 기준으로 두 수가 각 변수에 저장된다.

입력 : 3:15
출력 : 3:15
'''
a, b = input().split(':')    # :을 기준으로 나눔
print('{}:{}'.format(a, b))


'''
[18]
년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.

입력
연, 월, 일이 ".(닷)"으로 구분되어 입력된다.
출력
입력받은 연, 월, 일을 yyyy.mm.dd 형식으로 출력한다.

입력 : 2020.2.9
출력 : 2020.02.09
(단, m 혹은 d가 한 자리 수인 경우 앞에 0을 붙여 출력한다.)
'''
y, m, d = input().split('.')
if len(m) == 1:
    m = '0'+m
if len(d) == 1:
    d = '0'+d
print('{}.{}.{}'.format(y, m, d))


'''
[19]
주민번호는 다음과 같이 구성된다.

XXXXXX-XXXXXXX

앞의 6자리는 생년월일(yymmdd)이고 뒤 7자리는 성별, 지역, 오류검출코드이다.
주민번호를 입력받아 형태를 바꿔 출력해보자.

입력
주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다.
(입력값은 가상의 주민번호이다.) ex)110011-0000000

출력
'-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.

입력 : 000907-1121112
출력 : 0009071121112
'''
i, j = input().split('-')
print(i+j)  # 내답

a, b = input().split('-')
print('{}{}'.format(a, b))   # 정답풀이


'''
[20]
1개의 문자열을 입력받아 그대로 출력해보자.
'''
string = input()
print(string)


'''
[22]
공백이 포함되어 있는 한 문장이 입력된다. 단, 입력되는 문장은 여러 개의 단어로 구성되고, 엔터로 끝난다.
'''
string = input()
print(string)


'''
[23]
실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.

입력 :
1.435867

출력 :
1
435867
'''
i = input().split('.')
print(i[0])
print(i[1])  # 내답

string = input().split('.')
print('''\
{}
{}
'''.format(string[0], string[1]))  # 정답


'''
[24]
단어를 1개 입력받는다.
입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.
(단, 단어의 문자(영어)를 하나씩 나누어 한 줄에 한 개씩 ' '로 묶어서 출력한다.)

입력 :
'Boy'

출력 :
'B'
'o'
'y'
'''
string = input()
for i in range(len(string)):  # string의 글자 수 만큼 반복
    print("'{}'".format(string[i]))


'''
[25]
다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.

입력 :
75254

출력 :
[70000]
[5000]
[200]
[50]
[4]
'''
five = input()
count = len(five)-1
for i in range(len(five)):
    print([int(five[i] + '0'*count)])
    count = count - 1


'''
[26]
입력되는 시:분:초 에서 분만 출력해보자.
'''
h, m, s = input().split(':')
print(m)


'''
[27]
년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.

년월일(yyyy.mm.dd)를 입력받아,

일월년(dd-mm-yyyy)로 출력해보자.

(단, 한 자리 일/월은 0을 붙여 두자리로 출력한다.)
'''
y, m, d = input().split('.')
m = '0'+m if len(m) == 1 else m
d = '0'+d if len(d) == 1 else d
print(d+"-"+m+"-"+y)
