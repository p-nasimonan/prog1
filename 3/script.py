# -*- coding: utf8 -*-

#レベル1「降水量の平均値を求めよ」
def average(rains:list[float]) -> float:
    total = 0.0
    for rain in rains:
        total += float(rain) #合計を求める
    res = total/len(rains) #合計/リストの長さ
    return res

daily_rains:list[float] = [2.0, 0.0, 0.5, 3.0, 21.0]
print(average(daily_rains))

#----------------------------------------------------------
#レベル2「降水量の分散を求めよ」

#Σの中に入れる関数
def function(x:list, i:int) -> float: 
    res = (x[i] - average(x))**2
    return res

#Σ関数
def sigma (max_n:int, start_n:int, x:list[float]) -> float: 
    res:float = 0.0
    for i in range(start_n, max_n+1):
        res += function(x, i-1)
    return res

#分散の関数
def bunsan(rains:list[float]) -> float:
    n:int = len(rains)
    res = 1/n * sigma(n , 1, rains)
    return res

#式通りの分散
daily_rains = [2.0, 0.0, 0.5, 3.0, 21.0]
print(bunsan(daily_rains))

#簡単な式でもやってみた
#リストを二乗する関数
def listSquare(list:list[float]) -> list[float]:
    res = [0.0] * len(list)
    for i in range(len(list)):
        res[i] = list[i] ** 2
    return res

#分散の関数ver2
def bunsan2(rains:list[float]) -> float:
    return average(listSquare(rains)) - average(rains)**2

print(f'簡易ver:{bunsan2(daily_rains)}')

print('---------')

#----------------------------------------------------------
#レベル3「分散の意味を考察せよ」
daily_rains = [2.0, 0.0, 0.5, 3.0, 21.0]
A1 = bunsan(daily_rains)
print(A1)

daily_rains = [7.0, 5.0, 5.5, 8.0, 26.0]
A2 = bunsan(daily_rains)
print(A2)  #変わらないはずだが...微妙に違う！！なぜ!
print(f'簡易ver:{bunsan2(daily_rains)}')
print(f"A1:{A1:.40f} \nA2:{A2:.40f}")
#多分2進数にうまく変換できなかったり割り切れなかったりするのかもdecimalとFractionを使うとうまくできるっぽい

daily_rains = [20.0, 0.0, 5.0, 30.0, 210.0]
print(bunsan(daily_rains)) #100倍された



#オプション課題

#float以外は除くようにする関数
def list_type_C(inlist:list) -> list[float]:
    outlist = []
    for i in inlist:
        if type(i) is float:
            outlist.append(i)
    return outlist

daily_rains = [2.0, 0.0, '--', 0.5, '', 3.0, 21.0]
daily_rains = list_type_C(daily_rains)

print(average(daily_rains))
print(bunsan(daily_rains))