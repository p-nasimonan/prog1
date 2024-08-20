"""# 課題レポート7: 原始的なインデキシングによる検索エンジンの実装
関数:
    open_file: 
        What:
            ## ファイルを開く
            - 指定されたパスのtxtを開き、{ファイル名:[内容1行目,2行目...]}を返す
        ----------------------------------------------------------------
        Why:
            ## 関数make_indexの処理で使うため
            - 関数を作ることで、ファイルを開く処理を簡潔に書けそうだと思った。
        ----------------------------------------------------------------
    
    make_index:
        What:
            ## indexを作る
            - 指定されたパスのtxtから{単語:[含まれていたファイル名]}を返す
        ----------------------------------------------------------------
        Why:
            ## 関数search_wordsで含まれる単語を調べる時に使うため
            - {単語:[含まれていたファイル名]}を作ることによって単語をkeyとして含まれるファイルを調べられる
        ----------------------------------------------------------------

    is_match_words:
        What:
            ## 単語が一致するか
            - 単語のリストと単語が一致するかのリストをyieldで返す
        ----------------------------------------------------------------
        Why:
            ## 関数search_wordsでネストが深くならないように作成
            - 機能としてわかりやすそうだから
        ----------------------------------------------------------------

    join_list:
        What:
            ## [[要素1],[要素2]]を[要素1, 要素2]にする
            - or, andで結合の仕方を変えられる。
            - or, andと明記するすることでどのように結合するかわかりやすい
        Why: 
            ## 関数search_wordsで一旦含まれていたファイル名がリストで複数出るようにしているからくっつけたい
        ----------------------------------------------------------------
    
    search_words:
        What:
            ## 単語が一致するファイルを検索する
            - indexと一致するか調べたい単語を入れて、一致するファイルを返す
        ----------------------------------------------------------------
        Why:
            ## この課題の目的
        ----------------------------------------------------------------

Example:
    #### 以降はPythonコード例 ####
    >>> import report7
    >>> filenames = ['file1.txt', 'file2.txt', 'file3.txt']

    # インデックス生成部
    >>> index = report7.make_index(filenames)
    >>> print(len(index))
    9
    >>> print(index)
    {'the': ['file1.txt', 'file2.txt', 'file3.txt'], 'cat': ['file1.txt', 'file3.txt'], 'sat': ['file1.txt', 'file3.txt'], 'on': ['file1.txt', 'file2.txt'], 'mat': ['file1.txt', 'file2.txt'], 'dog': ['file2.txt', 'file3.txt'], 'stood': ['file2.txt', 'file3.txt'], 'while': ['file3.txt'], 'a': ['file3.txt']}

    # マッチング部その1: 「cat」検索結果
    >>> print(report7.search_words(index, ['cat']))
    ['file1.txt', 'file3.txt']

    # マッチング部その2: 「cat dog」検索結果
    >>> print(report7.search_words(index, ['cat', 'dog']))
    ['file3.txt']

    # マッチング部その3: 「cat mat on」検索結果
    >>> print(report7.search_words(index, ['cat', 'mat', 'on']))
    ['file1.txt']

    # マッチング部その4: 「hoge」検索結果（該当なしの例）
    # 'None'という文字列を返すのではなく、NoneType型のNoneを返す点に注意。
    >>> print(report7.search_words(index, ['hoge']))
    None
    >>> print(type(report7.search_words(index, ['hoge'])))
    <class 'NoneType'>
"""


def open_file(file_names: list[str]) -> dict[str, list[str]]:
    """ファイルを開く
    
    Args:
        file_names: ファイルのパスのリスト

    Returns:
        file_contents: {ファイル名:ファイルの内容}
    
    Example:
    >>> filenames = ['file1.txt', 'file2.txt', 'file3.txt']
    >>> print(open_file(filenames))
    {'file1.txt': ['the cat sat on the mat'], 'file2.txt': ['the dog stood on the mat'], 'file3.txt': ['the cat stood while a dog sat']}
    """
    file_contents = {}
    for file_name in file_names:
        with open(file_name, 'r') as f:
            lines = f.read().splitlines()  # ファイルを読み込み、行ごとにリストにする
        file_contents[file_name] = lines  # dictにファイル名と内容を追加する
    return file_contents


def make_index(file_names: list[str]) -> dict[str, list[str]]:
    """indexを作る
    Args:
        file_names: ファイルのパスのリスト

    Returns:
        words_index: {単語: [単語が含まれているファイル]}
    
    Example:
    >>> filenames = ['file1.txt', 'file2.txt', 'file3.txt']
    >>> print(make_index(filenames))
    {'cat': ['file1.txt', 'file3.txt'], 'mat': ['file1.txt', 'file2.txt'], 'on': ['file1.txt', 'file2.txt'], 'sat': ['file1.txt', 'file3.txt'], 'the': ['file1.txt', 'file2.txt', 'file3.txt'], 'dog': ['file2.txt', 'file3.txt'], 'stood': ['file2.txt', 'file3.txt'], 'a': ['file3.txt'], 'while': ['file3.txt']}
    """
    file_contents = open_file(file_names)
    words_index: dict[str, list[str]] = {}

    for filename, lines in file_contents.items():
        # ファイルの内容を一つの文字列に結合し、単語に分割
        all_text = ' '.join(lines)
        words = all_text.split()
        
        # 重複をなくし、単語をソート
        unique_words = sorted(set(words))
        
        for word in unique_words:
            if word not in words_index:
                words_index[word] = []
            words_index[word].append(filename)
    
    return words_index

#Generatorの戻り値はimportしないと書けない

def is_match_words(words: list[str], target_word: str):
    """単語のリストが単語に合っているか
    Args:
        words: [単語, 単語]
        target_word: 単語

    Generator:
        is_match_words: 単語が一致するか
    
    Example:
        >>> words = ['cat', 'mat', 'on']
        >>> target_word = 'mat'
        >>> print([i for i in is_match_words(words, target_word)])
        [False, True, False]

    """
    yield from (word == target_word for word in words)


def join_list(list_of_lists: list[list[str]], logical_operator: str) -> list[str]:
    """リストのリストを結合して文字列のリストに変換
    Args:
        list_of_lists: [リスト、リスト...]
        logical_operator: orまたはand

    Return: 
        result: [リスト内の要素、リスト内の要素...]
    
    Example:
        >>> join_list([['file1', 'file2'], ['file1', 'file3'], ['file1']], 'and')
        ['file1']
        >>> join_list([['file1', 'file2'], ['file2', 'file4'], ['file3']], 'and')
        []
    """
    result:set[str] = set()
    set_files:list[set] = list(map(set, list_of_lists))
    # 空じゃなければ
    if len(list_of_lists) != 0:
        result = set_files[0]

        # orの場合
        if logical_operator == 'or':
            for set_file in set_files:
                result |= set_file

        # andの場合
        elif logical_operator == 'and':
            for set_file in set_files:
                result &= set_file
        else:
            raise Exception(f'Error: {logical_operator}is not "and" or "or" ')
    

    return sorted(list(result))

def search_words(index: dict[str, list[str]], words: list[str], logical_operator: str = 'and') -> list[str] | None:
    """単語を検索する
    Args:
        index: {単語: [含まれているファイル]}
        words: [検索したい単語]
        logical_operator: orまたはand
    Return:
        result: 検索結果（ファイル名）

    """
    file_lists = []
    for word in words:
        if word in index:
            file_lists.append(index[word])

    result = join_list(file_lists, logical_operator)

    # resultが空のリストならNoneを出力
    return result if result else None