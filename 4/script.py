# レベル1「ユニークな単語一覧を作成し、出現回数を数えよ」
'''
文書はstr型で実行例のように用意するとする。文書を引数として受け取り、
単語ごとの出現回数を数えあげる関数を実装せよ。関数名を count_unique_words とする。

実行例
    doc1 = "I have a pen"
    result1 = count_unique_words(doc1)
    print(type(result1))
    <class 'dict'>
    print(result1)
    {'i': 1, 'have': 1, 'a': 1, 'pen': 1}
'''

def count_unique_words(Doc:str) -> dict:
    #文字列を単語ごとに分けてリストに変換
    doc:str = Doc.lower() #lowerメソッドで小文字に変換
    docs:list = doc.split() #指定がなければ空白で単語を分けてリストに変換する
    
    #リストの要素から単語の出現回数を調べる
    words:dict ={}
    for key in set(docs): #listを集合に変えてforの回数を減らす
        words[key] = docs.count(key) #countメソッドでkeyの文字列が何回あるかを辞書に追加
    return words
doc1 = "I have a pen"
result1 = count_unique_words(doc1)
print(type(result1))
print(result1) #setにして実行したから順序はない
#{'have': 1, 'pen': 1, 'a': 1, 'i': 1}

# レベル2「単語一覧を作成せよ」
'''
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

make_word_list関数の流れ

入力 docs:list 出力 (word_list:set, sentence_words:list) 


1,word_list(リスト全体の単語の集合)を出力する。

リストdocsの要素を結合してstrに変換  ←joinメソッドで要素を結合
    ↓
文字列を単語に分ける splitメソッドで空白を元に分ける
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

def make_word_list(Docs:list[str]) -> tuple[set, list]:
    words:str = (" ".join(Docs))  #joinで要素を結合
    word_list = set(words.split()) #splitで単語を分けてリストにする。それを集合に変換
    
    sentence_words:list = [dict()]*len(Docs) #最初に指定した方がメモリに優しそう
    for i in range(len(Docs)):
        sentence_words[i] = count_unique_words(Docs[i])

    return word_list, sentence_words

docs = ['I have a pen', 'I have an apple']
# 単語一覧を作成、ついでにレベル1の結果も返す
word_list, sentence_words = make_word_list(docs)
print(type(word_list))
print(word_list)
print(type(sentence_words))
print(sentence_words)

#オプション
'''
単語文書行列について知らなかったため調べた


'''