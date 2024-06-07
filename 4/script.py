
'''
=====================================================================
レベル1「ユニークな単語一覧を作成し、出現回数を数えよ」

文書はstr型で実行例のように用意するとする。文書を引数として受け取り、
単語ごとの出現回数を数えあげる関数を実装せよ。関数名を count_unique_words とする。

実行例
    doc1 = "I have a pen"
    result1 = count_unique_words(doc1)
    print(type(result1))
    <class 'dict'>
    print(result1)
    {'i': 1, 'have': 1, 'a': 1, 'pen': 1}
=====================================================================
レベル2「単語一覧を作成せよ」

文書集合はリスト型で実行例のように用意するとする。
文書集合を引数として受け取り、単語一覧を作成する関数を実装せよ。
関数名を make_word_list とする。
なお、make_word_list内部ではレベル1で作成した関数count_unique_wordsを利用すること。

実行例
    # 2文書を用意
    docs = ['I have a pen', 'I have an apple']

    # 単語一覧を作成、ついでにレベル1の結果も返す
    word_list, sentence_words = make_word_list(docs)
    print(type(word_list))
    <class 'set'>
    print(word_list)
    {'a', 'apple', 'i', 'have', 'pen', 'an'}
    print(type(sentence_words))
    <class 'list'>
    print(sentence_words)
    [{'i': 1, 'have': 1, 'a': 1, 'pen': 1}, {'i': 1, 'have': 1, 'an': 1, 'apple': 1}]
    =====================================================================
'''

# レベル1「ユニークな単語一覧を作成し、出現回数を数えよ」
def count_unique_words(Doc:str) -> dict[str, int]:
    '''
    入力:文字列
    出力:dict[単語, 出現回数]
    '''
    #文字列を単語ごとに分けてリストに変換
    doc:str = Doc.lower() #lowerメソッドで小文字に変換
    docs:list = doc.split() #指定がなければ空白で単語を分けてリストに変換する
    
    #リストの要素から単語の出現回数を調べる
    words = {k:docs.count(k) for k in set(docs)}
    return words
doc1 = "I have a pen"
result1 = count_unique_words(doc1)
print(type(result1))
print(result1) #setにして実行したから順序はない
#{'have': 1, 'pen': 1, 'a': 1, 'i': 1}

del doc1, result1

# レベル2「単語一覧を作成せよ」
def make_word_list(Docs:list[str]) -> tuple[set[str], list[dict[str, int]]]:
    '''
    入力 list[文字列,文字列...]
    出力 (set[複数の文字列の全体の単語一覧], dict[リストの要素それぞれの単語(key), 単語数(value)])


    1,word_list(リスト全体の単語の集合)を出力する。

    リストdocsの要素を結合してstrに変換  ←joinメソッドで要素を結合
        ↓
    文字列を単語に分ける splitメソッドで空白を元に文章を単語に分割
        ↓
    setに変換
        ↓
    word_list

    2,sentence_words(リストの要素それぞれの単語(key)と単語数(value))を出力する
    リストdocsを文字列に分けて処理する
            ↓
        文字列をレベル1で作ったcount_unique_wordsに入れる
            ↓
    sentence_words
    '''
    words:str = (" ".join(Docs))  #joinで要素を結合
    word_list = set(words.split()) #splitで単語を分けてリストにする。それを集合に変換
    
    sentence_words:list = [dict()]*len(Docs) #最初に指定した方がメモリに優しそう
    for i in range(len(Docs)):
        sentence_words[i] = count_unique_words(Docs[i]) #レベル1の関数で単語に分ける

    return word_list, sentence_words

docs = ['I have a pen', 'I have an apple']
# 単語一覧を作成、ついでにレベル1の結果も返す
word_list, sentence_words = make_word_list(docs)
print(type(word_list))
print(word_list)
print(type(sentence_words))
print(sentence_words)

del docs, word_list, sentence_words
#オプション
'''
単語文書行列について知らなかったため調べた

chatgptに聞いてみた（ドキュメントに添付してある）
単語文書行列を使うと、文書同士がどれだけ似ているか調べることができるらしい

調べるとTF-IDFという方法を使って解析するらしい

TF値は、文書内における「ある単語の出現頻度」を指します。
要は、文書内にある全ての単語の出現回数に対し、
その単語の出現回数がどれほどを占めるかという割合を表すものと理解すればよいでしょう。
その単語の出現回数が多ければTF値は大きくなり、逆に出現回数が低ければ、TF値が下がるしくみです。

IDF値は、「文書集合体の中にある単語が含まれる文書の割合の逆数」を表します。
その単語が他の文書中でも多く出現していればIDF値は小さく、他の文書にあまり出現していないほどIDF値は大きいということです。
(https://sirprize.co.jp/meo/word/tf-idf/#:~:text=TF%2DIDF%E5%80%A4%E3%81%AE%E6%AC%A0%E7%82%B9,-%E6%96%87%E6%9B%B8%E5%86%85%E3%81%AB&text=%E3%81%9D%E3%81%AE%E7%90%86%E7%94%B1%E3%81%AF%E3%80%81%E3%80%8CTF%E5%80%A4,%E5%BD%B1%E9%9F%BF%E3%81%97%E3%81%A6%E3%81%97%E3%81%BE%E3%81%84%E3%81%BE%E3%81%99%E3%80%82)

つまり単語に分けて、頻度を調べて比較とかする

これを実装するには、出現回数を調べて二つの文章を比較する
'''