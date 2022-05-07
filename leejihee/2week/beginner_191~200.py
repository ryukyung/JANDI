# 191
# data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.
# 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for row in data:
    for col in row:
        print(col*(1+0.00014))

# 192
# 191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.
for row in data:
    for col in row:
        print(col*(1+0.00014))
    print("----")

'''
193
192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.

>> print(result)
[2000.28, 3050.427, 2050.2870000000003, 1980.2772, 7501.05, 2050.2870000000003, 2050.2870000000003, ...]
'''
result = []
for row in data:
    for col in row:
        result.append(col*(1+0.00014))
print(result)

'''
194
191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.

>> print(result)
[
 [2000.28, 3050.427, 2050.2870000000003, 1980.2772],
 [7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772],
 [15452.163, 15052.107, 15552.177, 14902.086000000001]
]
'''
result = []
for row in data:
    sub = []
    for col in row:
        sub.append(col*(1+0.00014))
    result.append(sub)
print(result)

'''
195
ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 화면에 종가데이터를 출력하라.

100
190
310
'''
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    print(row[3])

'''
196
ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.

190
310
'''
for row in ohlc[1:]:
    if row[3] > 150:
        print(row[3])

'''
197
ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.

100
310
'''
for row in ohlc[1:]:
    if row[0] <= row[3]:
        print(row[3])

'''
198
ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.

>> print(volatility)
[40, 30, 10]
'''
volatility = []
for row in ohlc[1:]:
    volatility.append(row[1]-row[2])
print(volatility)

'''
199
리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.    
종가가 시가보다 높은 거래일의 OHLC는 [300, 310, 300, 310] 이다. 따라서 이 거래일의 변동성은 10 (310 - 300)이다.

10
'''
for row in ohlc[1:]:
    if row[3] > row[0]:
        print(row[1]-row[2])

'''
200
리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
1일차 수익 0원 (100 - 100), 2일차 수익 -10원 (190 - 200), 3일차 수익 10원 (310 - 300) 이다.

0
'''
total = 0
for row in ohlc[1:]:
    total = total + row[3]-row[0]
print(total)
