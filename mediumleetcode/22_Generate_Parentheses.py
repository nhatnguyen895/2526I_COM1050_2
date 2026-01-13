class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtracking(n,a,left,right):
            if len(a)==2*n:
                ans.append(a)
                return 
            if left<n:  
                a+="("
                backtracking(n,a,left+1,right)
                a=a[0:len(a)-1]
            if left>right:
                a+=")"
                backtracking(n,a,left,right+1)
                a=a[0:len(a)-1]
        backtracking(n,"",0,0)
        return ans
