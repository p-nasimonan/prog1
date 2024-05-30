# -*- coding: utf8 -*-
import math
#---LEVEL1---- 
def init_app(): #関数を定義する
    print('Welcome!')

#関数を実行する
init_app()


#---LEVEL2---- 
def init_app2(size:int): #関数を定義する
    hash = '#' * size #size個ハッシュタグをhashに代入
    print(f'{hash}Welcome!{hash}') #f-str

#関数を実行する
init_app2(2)


#---LEVEL3---- 
def init_app3(size:int, name:str): #関数を定義する
    hash = '#' * size

    if name == '': #nameが何もなかったらnew player
        usr_name = 'new player'
    else:
        usr_name = name

    print(f'{hash}Welcome {usr_name}! {hash}')

#関数を実行する
init_app3(2, '')  #名前がない場合

init_app3(2, 'ryutoku')  #名前がある場合


#---LEVEL4---- 
def f(x:float):#関数を定義する(数学ライブラリーを使わずにやってみる)
    #resultを増やしていって目標に近づくようにしたら解けるのでは
    #config--------
    distance:float = 0.00001  #二乗した答えとxの差がどれほど離れているか
    result_v0:float = 0.5  #答えを増やす速度
    result_vmulti:float = 0.8  #速度に毎回かける数。傾き
    result:float = 0.0  #答えの初期値
    #--------------

    result_v:float = result_v0 #あとで使えるように保持しておく

    while abs(x - result**2) > distance:
        result_v *= result_vmulti
        if x - result**2 < distance:
            while x - result**2 < distance :
                result -= result_v
        else:
            while x - result**2 > distance :
                result += result_v

    return result

#関数を実行する
result = f(10)
print(f"{result=:.5f}")

#オプション1------
#時間があったらやる

#オプション1:数値微分の実装

def numerical_derivative(function, x, h):
    #間違えた式↓
    # return (function(x+h) - function(x))/h
    #0.25002 じゃなくて 0.24846が出た。→あとで式をよく確認したところかなり式が違った
    return (function(x+h) - function(x-h))/(2*h)

def f2(x):
    return math.sqrt(x)
result = numerical_derivative(f2, 4, 0.1)
print(f"{result=:.5f}")

#式を書くだけだったから簡単だった。関数を関数に入れることは普通にできるんだとわかった

#オプション2:数値微分の考察

#まず関数電卓で計算してみる

#f2関数の結果を確認
print(f"{f2(4)=:.5f}")#√4=2問題なし

