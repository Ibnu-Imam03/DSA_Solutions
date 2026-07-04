class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        s=0
        for j in range(len(strs[0])):
            for i in range(len(strs)-1):
                 if strs[i][j]<=strs[i+1][j]:
                   continue
                 else :
                    s+=1 
                    break  
        return s            