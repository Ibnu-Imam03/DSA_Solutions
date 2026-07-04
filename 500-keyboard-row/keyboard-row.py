class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        n=set(list("qwertyuiop"))
        m=set(list("asdfghjkl"))
        b=set(list( "zxcvbnm"))
        l=[]
        for i in words:
            w=set(list(i.lower()))
            if w<=n or w<=m or w<=b :
                l.append(i)
             
        return l 