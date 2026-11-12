class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        m=max(nums)
        b=nums.index(m)
        for i in nums:
            if i!=m and m<2*i:
                return -1
        return b
        
                



        