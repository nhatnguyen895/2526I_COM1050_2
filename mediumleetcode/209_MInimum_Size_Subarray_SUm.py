class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Min=10**6
        i=0
        a=0
        for j in range(len(nums)):
            a+=nums[j]
            while a>=target:
                if j-i+1<Min:
                    Min=j-i+1
                a-=nums[i]
                i+=1
        if Min==10**6:
            return 0
        else:
            return Min