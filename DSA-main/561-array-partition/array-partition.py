class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
       nums.sort()
       s=0
       m=0
       n=1
       while True :
          if n<len(nums):
            s+=min(nums[m],nums[n])
            m+=2
            n+=2
          else:
            break  
       return s     
         
