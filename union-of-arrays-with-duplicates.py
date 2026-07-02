class Solution:    
    def findUnion(self, a, b):
        # code here
        return len(set(a)|set(b))
        