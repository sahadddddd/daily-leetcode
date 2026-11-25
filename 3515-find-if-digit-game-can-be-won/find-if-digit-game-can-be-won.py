class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        double=0
        single=0
        for i in nums:
            if i>=10:
                single+=i
            else:
                double+=i
        if double>single or single>double:
            return True
        else:
            return False
