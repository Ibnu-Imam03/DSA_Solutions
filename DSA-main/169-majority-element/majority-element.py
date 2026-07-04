class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        s=len(set(nums))
        k={}
        for i in range(s):
                k[nums.count(nums[0])]=nums[0]
                nums=nums[nums.count(nums[0]):]
        w=list(k.keys())
        ww=max(w)
        return k[ww]
               