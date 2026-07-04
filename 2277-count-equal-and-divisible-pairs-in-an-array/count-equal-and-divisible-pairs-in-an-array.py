class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        j=True
        c=0
        if len(set(nums))==len(nums):
            return 0

        else:
         for i in range(len(nums)):
          for j in range (i+1,len(nums)):
            if nums[i]==nums[j] and i*j%k==0:
                c+=1

        return c 