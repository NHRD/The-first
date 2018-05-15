class Solution(object):

    def __init__(self, x):
        self.x = x
        self.nums =[]

    def reverse(self):
        for i in self.x:
            self.nums.append(i)
        return self.nums
    
    def pop_num(self):
        return self.nums.pop()

num = input("Input int number:")
result = Solution(num)
result.reverse()
reverse = ""

if int(num) >= 0:
    for i in num:
        reverse += result.pop_num()
else:
    num_r = num[1::]
    for i in num_r:
        reverse += result.pop_num()
    reverse =  "-" + reverse 

print(reverse)