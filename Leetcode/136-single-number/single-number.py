class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k={}
        for i in nums:
            if i in k.keys():
                del k[i]
            else:
                 k[i]=1       
        
        for i in  k.keys() :
            return i        
        