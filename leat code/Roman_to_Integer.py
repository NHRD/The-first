class Solution:

    def __init__(self,s):
        dict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        self.s = s
    
    def sum(self):
        self.sum = 0
        for i in self.s:
            if i != "V" and i != "X" and i != "I" :
                self.sum = self.sum + self.dict[i]
        return self.sum

result = Solution("II")
print(result.sum())

                
