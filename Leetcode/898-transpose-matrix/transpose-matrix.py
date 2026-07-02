class Solution:
    def transpose(self, List: List[List[int]]) -> List[List[int]]:
        col=len(List[0])
        row=len(List)
        l=[]
        for i in range (col):
              k=[]
              for j in range(row):
                  k.append(List[j][i])
              l.append(k)    
        return l      