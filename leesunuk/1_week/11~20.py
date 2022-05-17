'''11번: 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요. '''
삼성전자=50000;총액=(삼성전자*10);print(총액)

'''12번: 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액(298조), 현재가(50,000), PER(15.79) 등을 바인딩해보세요.

내답: 시가총액=2980000000000;현재가=50000;PER=15.79;print("시가총액=",시가총액);print("현재가=",현재가);print("PER=",PER)
이렇게 생각한 이유: 변수를 만들어 그안에 각각 변수값을 넣어주고 print로 출력하면 될 거 같았다.

해답:
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

결과: 내가 생각한 답                    해답결과
시가총액 = 298000000000000          298000000000000 <class 'int'>
현재가 = 50000                      50000 <class 'int'>
PER = 15.79                         15.79 <class 'float'>
'''

'''13번: 변수 s와 t에는 각각 문자열( s = "hello", t = "python")이 바인딩 되어있습니다, 두 변수를 이용하여 hello! python와 같이 출력하세요

내답: s = "hello"; t = "python" ; print(s,"!",t)
생각한 이유: s와 t에 이미 hello 와 python이라는 값이 바인딩 되어 있고, hello! python과 같이 출력하기 위해선 print문에 !만 추가해서 같이
출력해주면 될 것 같았다. 이미 저번 문제에서 이렇게 출력하면 띄어쓰기가 되어 나온다는 걸 인지하고 있었으나, 방법이 떠오르지 않아서 위와같은
시도를 해봤다.

해답: s = "hello"; t = "python" ; print(s+"!",t)

'''

'''14번: 2 + 2 * 3 코드 실행 결과를 예상해보세요.
내답: 8 '''

'''15번: 아래 변수(a = "132")에 바인딩된 값의 타입을 판별해보세요.

내답: print(a, type(a))
이렇게 생각한 이유: a에 바인딩되어 있는 값을 출력해야 되니깐 a값도 같이 나오면 좋겠어서 a도 같이 프린트 했다.

해답:a="132"; print(type(a))
a값이 이미 입력이 되어있고, 바인딩된 값의 타입만 판별하면 될 줄 알았으나 a값도 넣으라는 것이었다. 다음부턴 유의해서 해야겠다. '''


'''16번: 문자열 '720'를 정수형으로 변환해보세요.

내답: int num_str = "720";print(num_str, type(num_str))

이렇게 생각한 이유: C에서 변수를 선언할때 보통 앞에 문자의 형태를 지정해주니까 똑같이 해주면 될 거 같았다.

해답: num_str = "720"; num_int=int(num_str); print(num_int, type(num_int))
새로운 변수를 선언해서 이미 있는 num_str을 int형으로 저장해야 된다.
'''

'''17번: 정수 100을 문자열 '100'으로 변환해보세요'''
num=100;N_num=str(num);print(N_num, type(N_num))

'''18번: 문자열 15.79를 실수 타입으로 변환해보세요'''
Nf_num="15.79";f_num=float(Nf_num);print(f_num, type(f_num)) 

'''19번": year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
내답: year="2020";i_year=int(year);for(i=0;i<3;i++){print(i_year);i_year=i_year-1;}
year 변수를 int형으로 변환했으니 for문을 돌려 year에 1씩 빼며 출력하면 될줄 알았다

해답:year = "2020";print(int(year)-3);print(int(year)-2);print(int(year)-1)
'''

'''20번:에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)'''
air=48584; hap=air*36; print("총금액=",hap)