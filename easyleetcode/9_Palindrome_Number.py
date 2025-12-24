class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        a=0
        b=len(x)-1
        while a<b:
            if x[a]==x[b]:
                a+=1
                b-=1
            else :
                return False
        return True