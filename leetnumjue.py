class Solution:

    def __init__(self, juel, stone):
        self.juel = juel
        self.stone = stone

    def numJewelsInStones(self):
        S = self.juel + self.stone
        return S
        """
        :type J: str
        :type S: str
        :rtype: int
        """

result = Solution(2, 3)
result2 = result.numJewelsInStones()
print(result2)