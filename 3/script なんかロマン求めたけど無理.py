# -*- coding: utf8 -*-

#レベル1「降水量の平均値を求めよ」
#降水量のデータを自動で取れるようにしてみたいからURLをダウンロードするためにurllib（標準ライブラリ）を使ってみた
import urllib.request
#BeautifulSoupはhtmlを解析するライブラリみたい
from bs4 import BeautifulSoup
def fetch_html(url: str) -> tuple[str,str]: #html取得 ->strで出力
    with urllib.request.urlopen(url) as res:
        html = res.read().decode()
        #インスタンスの作成
        soup = BeautifulSoup(res, 'html.parser')

    return html, soup
jma_html, jma_soup = fetch_html("https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=91&block_no=47936&year=2021&month=1&day=&view=")

#htmlをタグと文字に分けたい
i:int = 0
j:int = 0
k:int = 0
tag = ['']
etc = ['']
while True:
    
    #<を見つけたらtag[]に追加して>が出るまでくっつける
    if jma_html[i] == '<' :
        tag.append('')
        while True:
            tag[j] = tag[j] + jma_html[i]
            #>を見つけたら終わる
            if jma_html[i] == '>': 
                if not jma_html[i+1] == '<': #<tag><tag>ってなっていなければ文字リストを追加する
                    etc.append('')
                    k += 1
                break
            i += 1
        j += 1
        
    else:
        if not jma_html[i] == '>':
            etc[k] = etc[k] + jma_html[i]
        i += 1
    if i == len(jma_html): #htmlと同じ文字数になったら終わる
        break 
#htmlをリストにしてやってみたはいいけどもうちょっと楽にしたい
print(tag)
print(etc)

elems =  jma_soup.select('.mtx')
for elem in elems:
    print(elem)