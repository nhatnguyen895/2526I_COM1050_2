class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def tapcon(nums,x):
            if x==1:
                return [[],[nums[x-1]]]
            a=tapcon(nums,x-1)
            b=tapcon(nums,x-1)
            for i in range(len(a)):
                a[i].append(nums[x-1])
            return b[0:]+a[0:]
        return tapcon(nums,len(nums))