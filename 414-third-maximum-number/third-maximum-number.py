class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l=list(set(nums))
        if len(l)<=2:
             return max(l)
        elif len(l)==3:
            return min(l)     
        else:
            k=max(l)
            l.remove(k)
            k=max(l)
            l.remove(k)
            return max(l)     
