class Solution:
    def uniqueMorseRepresentations(self, w: List[str]) -> int:
        f=set()
        c='abcdefghijklmnopqrstuvwxyz'
        ww=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(len(w)):
            r=''
            a=w[i]
            for j in range(len(w[i])):
                e=a[j]
                e=c.index(e)
                r+=ww[e]
            f.add(r)    
        return len(f)    
        