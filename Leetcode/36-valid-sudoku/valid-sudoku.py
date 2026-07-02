class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num='123456789'
        for i in range (len(board)):
            p=[]
            c=[]
            for j in range (len(board)):
                if board[i][j] in num:
                       p.append(board[i][j])
                if board[j][i] in num:       
                       c.append(board[j][i])
                l=[]
                for k in range(3):
                    h=[]
                    for t in range(3):
                        if ( i ==0 or i==3 or i==6) and (j==0 or j==3 or j==6):
                          if board[i+k][j+t] in num:
                                h.append(board[i+k][j+t])
                    if len(h)>1:        
                        l.extend(h)
                    elif h==[]:
                        jjj=0
                    else :
                        l.append(h[0])    
                ll=l.copy()
                if len(l)!=len(set(ll)) :
                    return False

            cc=c.copy()
            pp=p.copy()           

            if len(c)!=len(set(cc))  or len(p)!=len(set(pp)) :
                return False           
        else:
            return True        