#!/usr/bin/env python
import collections
import sys

def find_longest_word_in_string(letters, words):
    letter_positions = collections.defaultdict(list)
#初期化不要のリストを作成するため。defaultdictを使用。


    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)
#lettersから文字を辞書のkeyとして取り出し。
#lettersの中のletterの位置を辞書にリストで格納。
#keyはletter。

    for word in sorted(words, key=lambda w: len(w), reverse=True):
        #wordsの中の単語を長さで降順ソート
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break
        #文字がletter_positionsになければbreak

        possible_positions = [p for p in letter_positions[letter] if p >= pos]
        if not possible_positions:
            break
        pos = possible_positions[0] + 1
        else:
            return word

if __name__ == '__main__':
    print(subdict(sys.argv[1], sys.argv[2:]))

#コマンドラインから直接スクリプトファイルを実行した場合は「__name__という変数（属性）の中に自動的に__main__を代入する」操作が一番はじめにで行われる。