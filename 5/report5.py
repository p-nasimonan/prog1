'''
課題レポート5: 基本的な自然言語処理を実装してみよう（その2）。
'''


#レベル1「ドキュメント、テストを書け」--------------------------------------------------------
def count_unique_words(Doc:str) -> dict[str, int]:
    '''
    ### 入力:文字列
    ### 出力:dict[単語, 出現回数]

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
    result_words = {k:docs.count(k) for k in sorted(set(docs), key=docs.index)} #順番が変わらないようにした
    return result_words

def make_word_list(Docs:list[str]) -> tuple[set[str], list[dict[str, int]]]:
    '''
    ### 入力 list[文字列,文字列...]
    ### 出力 (set[複数の文字列の全体の単語一覧], dict[単語(key), 単語数(value)])

    2文書を用意
    >>> docs = ['I have a pen', 'I have an apple']

    単語一覧を作成、ついでにレベル1の結果も返す
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
    Words:str = (" ".join(Docs))  #joinで要素を結合
    words = Words.lower() #lowerメソッドで小文字に変換
    word_list = words.split() #splitで単語を分けてリストにする。
    result_word_set:set = set(sorted(word_list)) #それを集合にする。前回、集合にしたときに順番が変わっていたためソートで並べ替えた
    #しかし集合に直すと意味がないことが分かった

    result_sentence_words:list = list(map(count_unique_words, Docs))  #map関数を使ってレベル1の関数で単語を数える
    #map関数(関数, シーケンス)->それぞれの要素を関数で実行

    return result_word_set, result_sentence_words


# レベル2「単語文書行列を作成せよ」---------------------------------------------------------------------------------
def make_word_doc_matrix(words:set, sentence_words:list[dict[str, int]]) -> tuple[list, list[list[int]]]:
    '''
    ### 入力 set[複数の文字列の全体の単語一覧], dict[単語(key), 単語数(value)]
    ### 出力 list[sorted(複数の文字列の全体の単語一覧)], 単語の出現回数
    >>> docs = ['I have a pen', 'I have an apple']
    >>> word_list, sentence_words = make_word_list(docs)

    >>> column_names, matrix = make_word_doc_matrix(word_list, sentence_words)
    >>> print(column_names)
    ['a', 'an', 'apple', 'have', 'i', 'pen']
    >>> print(matrix)
    [[1, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0]]
    '''

    result_words:list = sorted(words) #集合から辞書順に並んだリストにする

    #matrixのリストを要素数を指定して宣言しておく
    result_matrix:list[list[int]] = [[0]*len(words)]*len(sentence_words) 
    i:int = 0 #カウント変数
    j:int = 0 #カウント変数
    for sentence_word in sentence_words:
        result_matrix[i] = [0]*len(words) #初期化しないといけない
        for word in result_words:
            if word in list(sentence_word):
                result_matrix[i][j] = sentence_word[word]
            j += 1
        i += 1
        j = 0

    return result_words, result_matrix


#オプション
import numpy as np
# 2つの点p, qの座標位置の配列を定義
# p = np.array([1, 3])
# q = np.array([4, 7])
# # 2点間のユークリッド距離を計算する
# dist = np.linalg.norm(p - q)
# print(dist) 
# 出力結果：5.0

#doctest
if __name__ == '__main__':
    import doctest
    doctest.run_docstring_examples(make_word_doc_matrix, globals(), verbose=True)