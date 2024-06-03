# レベル1「ユニークな単語一覧を作成し、出現回数を数えよ」

def count_unique_words(DOC:str) -> dict:
    #文字列を単語ごとに分けてリストにまとめる
    doc:str = DOC.lower() #lowerメソッドで小文字に変換
    doclist:list = doc.split() #指定がなければ空白で単語を分けてリストに変換する
    
    #listの要素から出現回数を調べる
    words:dict ={}
    for key in set(doclist): #listを集合に変えてforの回数を減らす
        words[key] = doclist.count(key) #countメソッドでkeyの文字列が何回あるか
    return words
doc1 = "I have a pen"
result1 = count_unique_words(doc1)
print(result1) #setにして実行したから順序なんてない

# レベル2「単語一覧を作成せよ」
def make_word_list(DOCs:list) -> tuple:
    for DOC in DOCs:
        count_unique_words(DOC)

docs = ['I have a pen', 'I have an apple']
word_list, sentence_words = make_word_list(docs)