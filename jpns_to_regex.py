import re


class JPNStoRegex:
    # 各トークンに対応する正規表現演算子登録
    token_table = {}
    token_table['タブ'] = '\t'
    token_table['任意の文字'] = '.'
    token_table['英数字'] = '\w'
    token_table['英数字以外'] = '\W'
    token_table['空白文字'] = '\s'
    token_table['空白文字以外'] = '\S'
    token_table['半角数字'] = '\d'
    token_table['半角数字以外'] = '\D'
    token_table['単語境界'] = '\b'
    token_table['か'] = '|'
    token_table['全角数字'] = '[０-９]'
    token_table['ひらがな'] = '[ぁ - ん]'
    token_table['カタカナ'] = '[ァ - ヴ]'
    token_table['半角カタカナ'] = '[ｦ - ﾟ]'
    token_table['('] = '('
    token_table[')'] = ')'

    token_table['が0回以上'] = '*'
    token_table['が1回以上'] = '+'
    token_table['が0回または1回'] = '?'

    token_table['行頭'] = '^'
    token_table['行末'] = '$'

    # 一部量指定子の検出及び置換用の正規表現登録
    match = r"が(\d+)回"
    match_repatter = re.compile(match)

    more = r"が(\d+)回以上"
    more_repatter = re.compile(more)

    more_less = r"が(\d+)回以上(\d+)回以下"
    more_less_repatter = re.compile(more_less)

    def __init__(self, text):
        self.text = text
        raw_tokens = text.split(' ')

        #半角スペース取得
        self.tokens = self.get_half_space(raw_tokens)

    def get_regex(self):
        text = ''
        for token in self.tokens:
            #トークンの先頭$で無条件で文字列として処理
            if token[0] is '$':
                token.pop[0]
                text += token
                continue
            if token in self.token_table.keys():
                #トークンを正規表現演算子に置き換え
                text += self.token_table[token]
                continue
            else:
                if self.more_less_repatter.match(token):
                    text += re.sub(self.more_less_repatter, "{\\1,\\2}", token)
                    continue
                if self.more_repatter.match(token):
                    text += re.sub(self.more_repatter, "{\\1,}", token)
                    continue
                if self.match_repatter.match(token):
                    text += re.sub(self.match_repatter, "{\\1}", token)
                    continue
            #文字列として処理
            text += token
        return text
    
    def get_half_space(self, raw_tokens):
        while '' in raw_tokens:
            index = raw_tokens.index('')
            if raw_tokens[index+1] == '':
                #2つの空要素を1つの半角スペースに変換
                raw_tokens.insert(index, ' ')
                raw_tokens.remove('')
                raw_tokens.remove('')
            else:
                #余分な空要素消去
                raw_tokens.remove('')
        return raw_tokens
