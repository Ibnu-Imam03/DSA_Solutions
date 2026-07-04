class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
            f={}
            l=[]
            for i in range (len(names)):
                   f[heights[i]] =names[i]
            c=list(f.items())  
            c.sort(reverse=True)  
            n=dict(c)   
            return list(n.values())
            

           