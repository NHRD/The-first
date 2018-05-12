import random

def hangman(word):
    wrong = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman.\nGuess the word below.")
    print(" ".join(board))
    while wrong < len(stages) - 1:
        char = input("Guess one character:")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose, the answer was {}.".format(word))

answers = ["cat","dog","elephant","playstation4","android","Ironman","xperia"]
answer = answers[random.randint(0,6)]

hangman(answer)
