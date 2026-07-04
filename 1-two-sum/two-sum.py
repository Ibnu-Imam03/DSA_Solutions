class Solution:
 def twoSum(self, nums: List[int], target: int) -> List[int]:
    m=0
    b=1
    while True :
     if nums[m]+nums[b]==target:
        return m,b
        break 
     elif m==len(nums)-2:
        break   
     elif b==len(nums)-1:
        m+=1
        b=m+1
     else :
        b+=1 
