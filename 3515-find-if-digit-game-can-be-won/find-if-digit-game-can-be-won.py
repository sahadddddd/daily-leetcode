class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        double=0
        single=0
        for i in nums:
            if i>=10:
                single+=i
            else:
                double+=i
        return False if single==double else True
