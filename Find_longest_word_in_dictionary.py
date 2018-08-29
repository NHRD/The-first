def find_longest_word_in_string(letter, words):
    i = 0
    ok = ""
    l = len(letter) - 1

    for w in words:
        j = 0
        while j < l:
            if w[0] == letter[j]:
                j += 1
                w = w[1:]
            else:
                j +=1
        if w == "":
            if len(ok) < len(words[i]):
                ok = words[i]
        i += 1

    return(ok)

S = "abppplee"
D = ["jam", "jamboleeee", "able", "ale", "apple", "bale", "kangaroo"]
result = find_longest_word_in_string(S, D)
print(result)