#011 변수 사용하기
#삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자=50000
total=삼성전자*10
print("총평가금액 : ", total)

#012 변수 사용하기
#다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print("시가 총액 : ", type(시가총액))
print("현재가 : ", type(현재가))
print("PER : ", type(PER))

#013 문자열 출력
#변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s="hello"
t="python"
print(s+"!", t)

#014 파이썬을 이용한 값 계산
#아래 코드의 실행 결과를 예상해보세요.
print(2+2*3)//3

#015 type 함수
a="128"
print(type(a))

#016 문자열을 정수로 변환
#문자열'720'를 정수형으로 변환해보세요.
num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int))

#017 정수를 문자열 100으로 변환
#정수 100을 문자열 '100'으로 변환해보세요.
num=100
result str(num)
print(result, type(result))

#018 문자열을 실수로 변환
#문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
data ="15.79"
data =float(data)
print(data, type(data))

#019 문자열을 정수로 변환
#year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year="2020"
print(int(year)-3)  # 2017
print(int(year)-2)  # 2018
print(int(year)-1)  # 2019

#020 파이썬 계산
#에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
월 = 48584
총금액 = 월 * 36
print(총금액)