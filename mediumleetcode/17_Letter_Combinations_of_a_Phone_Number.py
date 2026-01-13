class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Map=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        numbers=[int(i) for i in digits]
        ans=[]
        def backtracking(numbers,a,ID):
            if len(a)==len(numbers):
                ans.append(a)
                return
            for i in Map[numbers[ID]]:
                a+=i
                backtracking(numbers,a,ID+1)
                a=a[0:len(a)-1]
        backtracking(numbers,"",0)
        return ans