'''
課題レポート5: 基本的な自然言語処理を実装してみよう（その2）。
'''

import numpy as np
#レベル1「ドキュメント、テストを書け」
def count_unique_words(Doc:str) -> dict[str, int]:
    '''
    入力:文字列
    出力:dict[単語, 出現回数]

    実行例
    >>> doc1 = "I have a pen"
    >>> result1 = count_unique_words(doc1)
    >>> print(type(result1))
    <class 'dict'>
    >>> print(result1)
    {'i': 1, 'have': 1, 'a': 1, 'pen': 1}
    '''
    doc:str = Doc.lower() #lowerメソッドで小文字に変換
    docs:list = doc.split() #指定がなければ空白で単語を分けてリストに変換する
    
    #リストの要素から単語の出現回数を調べる
    words = {k:docs.count(k) for k in sorted(set(docs), key=docs.index)} #順番が変わらないようにした
    return words


# レベル2「単語一覧を作成せよ」
def make_word_list(Docs:list[str]) -> tuple[set[str], list[dict[str, int]]]:
    '''
    入力 list[文字列,文字列...]
    出力 (set[複数の文字列の全体の単語一覧], dict[リストの要素それぞれの単語(key), 単語数(value)])

    # 2文書を用意
    >>> docs = ['I have a pen', 'I have an apple']

    # 単語一覧を作成、ついでにレベル1の結果も返す
    >>> word_list, sentence_words = make_word_list(docs)
    >>> print(type(word_list))
    <class 'set'>
    >>> print(word_list)
    {'a', 'apple', 'i', 'have', 'pen', 'an'}
    >>> print(type(sentence_words))
    <class 'list'>
    >>> print(sentence_words)
    [{'i': 1, 'have': 1, 'a': 1, 'pen': 1}, {'i': 1, 'have': 1, 'an': 1, 'apple': 1}]
    '''
    words:str = (" ".join(Docs))  #joinで要素を結合
    word_list = set(words.split()) #splitで単語を分けてリストにする。それを集合に変換
    
    sentence_words:list = list(map(count_unique_words, Docs))  #map関数を使ってレベル1の関数で単語に分ける
    #map関数(関数, シーケンス)->それぞれの要素を関数で実行

    return word_list, sentence_words

#オプション
# 2つの点p, qの座標位置の配列を定義
p = np.array([1, 3])
q = np.array([4, 7])
# 2点間のユークリッド距離を計算する
dist = np.linalg.norm(p - q)
print(dist) 
# 出力結果：5.0