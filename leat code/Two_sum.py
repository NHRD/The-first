class Solution:
    num_pair = []
    def __init__(self):
        self.num = []
    
    def twoSum(self, nums, target):
        self.target = target
        for i in nums:
            self.num.append(i)
        for j in self.num:
            for k in self.num:
                if j + k == self.target:
                    self.num_pair.append([j,k])
                    self.num.remove(j)
                    self.num.remove(k)
        return self.num_pair
             

solution = Solution()
nums = []

try:
    while True:
        get_num = input("Input int nums, quit to input 'q':")
        nums.append(int(get_num))
        if get_num == "q":
            False
except: TypeError
print(nums)

target_val = int(input("Input target int number:"))

result = solution.twoSum(nums, target_val)

print(result)