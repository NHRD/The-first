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
for c in num:
    reverse += result.pop_num()

if int(num) < 0:
    print("From left to right, it reads {}. From right to left, it becomes {}. Therefore it is not a palindrome.".format(num, reverse))

elif int(num) == 0:
    print("From left to right, it reads {}. From right to left, it becomes {}. Therefore it is not a palindrome.".format(num, num)) 

elif int(num) > 0:
    if num == reverse:
        print("True")
    else:
        print("From left to right, it reads {}. From right to left, it becomes {}. Therefore it is not a palindrome.".format(num, reverse)) 