class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for I in range(max(nums)):
            if I not in nums:
                 return I
        else:
             return (max(nums) + 1)
