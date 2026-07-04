class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        x=list(str(x))
        if list(x[::-1])==list(x):
            return True
        else :
            return False    