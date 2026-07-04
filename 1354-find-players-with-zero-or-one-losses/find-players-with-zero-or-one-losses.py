class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win={}
        lose={}
        loose={}
        for i,j in matches:
            win[i]=1
            if j not in lose and j not in loose:
                lose[j]=1
            else:
                if j in lose:
                    loose[j]=1
                    del lose[j]
        won=list(win.keys())
        for i in won:
            if i in loose or i in lose:
                del win[i]
        f=list(lose.keys())
        g=list(win.keys())
        return [sorted(g),sorted(f)]