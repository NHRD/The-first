class HangmanLexicon:
    
    def getWordCount(self):
        self.num = 10
        return self.num
    
    def getWord(self, index):
        self.index = index
        if self.index == 0:
            self.answer = "BUOY"
            return self.answer
        elif self.index ==1:
            self.answer = "COMPUTER"
            return self.answer
        elif self.index ==2:
            self.answer = "CONNOISSEUR"
            return self.answer
        elif self.index ==3:
            self.answer = "DEHYDRATE"
            return self.answer
        elif self.index ==4:
            self.answer = "FUZZY"
            return self.answer
        elif self.index ==5:
            self.answer = "HUBBUB"
            return self.answer
        elif self.index ==6:
            self.answer = "KEYHOLE"
            return self.answer
        elif self.index ==7:
            self.answer = "QUAGMIRE"
            return self.answer
        elif self.index ==8:
            self.answer = "SLITHER"
            return self.answer
        elif self.index ==9:
            self.answer = "ZIRCON"
            return self.answer
        else:
            print("getWord: Illegal index")
    
    def array_pre(self, inty):
        self.index = inty
        self.ans = self.getWord(self.index)
        print(self.ans)
        self.ans_array = []
        self.disp_array =[]
        for c in self.ans:
            self.ans_array.append(c)
            self.disp_array.append("_")
        return self.ans_array, self.disp_array
    
    def main_game(self):
        print("Hangman")
        self.mode = int(input("input index:"))
        self.array_pre(self.mode)
        i = 0
        game = False
        while i < len(self.ans_array):
            print(" ".join(self.disp_array))
            if "_" not in self.disp_array:
                game = True
                break
            guess = input("Input guess char:")
            if guess.lower() in self.ans_array:
                cind = self.ans_array.index(guess.lower())
                self.ans_array[cind] = "$"
                self.disp_array[cind] = guess.lower()
            elif guess.upper() in self.ans_array:
                cind = self.ans_array.index(guess.upper())
                self.ans_array[cind] = "$"
                self.disp_array[cind] = guess.upper()
            else:
                i += 1
        if game == True:
            print("You win.")
        else:
            print("You loose.")

test = HangmanLexicon()
test.main_game()