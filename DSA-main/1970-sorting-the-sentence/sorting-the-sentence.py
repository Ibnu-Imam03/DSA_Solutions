class Solution:
    def sortSentence(self, s: str) -> str:
        n=(s.split())
        l=''
        k={}
        for i in n:
            k[i[-1]]=i[:-1]
        k=list(k.items())
        k.sort()
        l+=k[0][1]
        for i in range(1,len(k)):
            l+=' '+k[i][1]
    
        return l        