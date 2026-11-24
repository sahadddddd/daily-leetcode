class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        num=len(candyType)//2
        types=len(set(candyType))
        if types>num:
            return num
        else:
            return types
            
        