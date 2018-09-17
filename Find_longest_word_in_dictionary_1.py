#!/usr/bin/env python
import collections
import sys
import logging

logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")

logging.disable(logging.DEBUG)

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
            logging.debug("word is {}, letter is {}." .format(word, letter))
            if letter not in letter_positions:
                break
            #文字がletter_positionsになければbreak

            possible_positions = [p for p in letter_positions[letter] if p >= pos]
            #pは対象のletterの位置。forループ内の途中のif文がbreakされてもposは加算されるため、
            #次の文字が判定対象になる。
            logging.debug("possible_positions are {}." .format(possible_positions))
            logging.debug("pos is {}." .format(pos))
            if not possible_positions:
                break
            logging.debug("possible_positions[0] is {}." .format(possible_positions[0]))
            pos = possible_positions[0] + 1
            #possible_positin[0]はletterの位置を格納したリストの先頭の数字を返す。
            #↑により、lettersの中で判定対象の文字を現在のletterより後の文字とする。
            #例：letters = "aaapplle"、word = "apple"の場合、
            #一周目のループのletterは"a"のため、possible_positions = (0, 1, 2)
            #次のループのposは0 + 1 = 1
            #次のループではletterは"p"のため、possible_positions = (3, 4)
            #次のループのposは3 + 1 = 4
            #次のループではletterは"p"だが、p >= posより4以上でが条件のため、
            #possible_positions = (4)
            
        #単語に含まれる文字が無くなるまでforが回った場合breakされず、その単語を返す。
        else:
            return word

    #print(find_longest_word_in_string(sys.argv[1], sys.argv[2:]))
    #コマンドラインから文字列と単語を指定して実行。

if __name__ == '__main__':

    letters = "abppplee"
    words = ["able", "ale", "apple", "bale", "kangaroo"]
    print(find_longest_word_in_string(letters, words))"""

#コマンドラインから直接スクリプトファイルを実行した場合は「__name__という変数（属性）の中に自動的に
# __main__を代入する」操作が一番はじめにで行われる。