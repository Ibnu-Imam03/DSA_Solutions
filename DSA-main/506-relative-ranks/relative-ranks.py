class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
          if len(score)==1:
                l=[0]*len(score)
                n=max(score)
                v=score.index(n)
                l[v]="Gold Medal"
                return l
          elif len(score)==2:
                     l=[0]*len(score)
                     n=max(score)
                     v=score.index(n)
                     l[v]="Gold Medal"
                     score[v]=-1
                     n=max(score)
                     v=score.index(n)
                     l[v]="Silver Medal"
                     return l
          else:           
            l=[0]*len(score)
            n=max(score)
            v=score.index(n)
            l[v]="Gold Medal"
            score[v]=-1
            n=max(score)
            v=score.index(n)
            l[v]="Silver Medal"
            score[v]=-1
            n=max(score)
            v=score.index(n)
            l[v]= "Bronze Medal"
            score[v]=-1
            for i in range(4,len(score)+1):
                  n=max(score)
                  v=score.index(n)
                  l[v]= str(i)
                  score[v]=-1
            return l
