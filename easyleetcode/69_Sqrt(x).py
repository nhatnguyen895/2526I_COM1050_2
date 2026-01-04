class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        j=x
        while i<=j:
            mid=(i+j)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                j=mid-1
            elif mid*mid<x:
                i=mid+1
        if mid*mid<x:
            return mid
        elif mid*mid>x:
            return mid-1