class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def combination(a,Sum,target,ID):
            if Sum==target:
                ans.append(a[:])
                return 
            if Sum>target:
                return
            for i in range(ID,len(candidates)):
                if Sum<target:
                    a.append(candidates[i])
                    Sum+=candidates[i]
                    combination(a,Sum,target,i)
                    a.pop()
                    Sum-=candidates[i]
        combination([],0,target,0)
        return ans