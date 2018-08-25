S = "abppplee"
D = ["jam", "jamboleeee", "able", "ale", "apple", "bale", "kangaroo"]

print("S:" + S)
print("D:{}" .format(D))

i = 0
ok = ""
l = len(S) - 1

for w in D:
    j = 0
    while j < l:
        if w[0] == S[j]:
            j += 1
            w = w[1:]
        else:
            j +=1
    if w == "":
        if len(ok) < len(D[i]):
            ok = D[i]
    i += 1

print(ok)