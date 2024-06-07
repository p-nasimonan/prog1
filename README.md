# prog1
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">

## 概要
琉球大学知能情報コースのプログラミングⅠの課題<br>
<a href = "https://github.com/naltoma/python_intro2021">naltomaの解説ページのソースコード</a><br>
ソースコードを載せてどこからでも開発できるようにするため

## report1　print()関数と変数の利用、用語整理。
<a href = "https://ie.u-ryukyu.ac.jp/~tnal/2024/prog1/static/report/report1_print_variable_terms.html">リンク</a><br>
ここは小学教育レベル
例えば
```
print("p-nasi" +"プログラミング1の授業へようこそ")
```
これらのプログラムはインタプリンタ上で実行したためソースコードはない

## report2　関数定義と条件分岐に慣れよう
<a href = "https://ie.u-ryukyu.ac.jp/~tnal/2024/prog1/static/report/report2_2024.html">リンク</a><br>
プログラミングやったことない人はここから大変かも
### Level 2: 引数ありの関数
私はmathモジュールを使わずにやった(自慢)
```
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
```

## report3
<a href = "https://ie.u-ryukyu.ac.jp/~tnal/2024/prog1/static/report/report3_iteration.html">リンク</a><br>
リストはpythonのfor文と相性が良い!

## report4
しっかり処理の手順の整理をしてプログラムを書こう！
