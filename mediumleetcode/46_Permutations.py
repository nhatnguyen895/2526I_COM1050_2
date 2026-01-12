class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def hoanvi(nums,x):
            if x==1:
                return [[nums[0]]]
            ans=[]
            for i in hoanvi(nums,x-1):
                for j in range(len(i)):
                    a=i[0:j] + nums[x-1:x]+i[j:]
                    ans.append(a)
                ans.append(i[0:]+nums[x-1:x])
            return ans
        return hoanvi(nums,len(nums))
            