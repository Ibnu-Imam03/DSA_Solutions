class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
            l=[]
            h=True
            n=m=c=0
            while h :
                if n==len(nums):
                    h=False    
                elif m==len(nums):
                    n+=1   
                    l.append(c)
                    m=0   
                    c=0           
                elif nums[n]>nums[m]:
                    m+=1
                    c+=1
                else:
                    m+=1
            return l        
