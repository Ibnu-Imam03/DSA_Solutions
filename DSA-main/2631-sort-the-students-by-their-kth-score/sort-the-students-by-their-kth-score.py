class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        l={}
        for i in range(len(score)):
            l[score[i][k]]=score[i]
        k=list(l.keys())
        p=[]
        k.sort(reverse=True)
        for i in k:
           p.append(l[i]) 
        return p   

