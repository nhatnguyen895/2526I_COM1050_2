class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a=0
        for i in range(k):
            a+=nums[i]
        i=0
        b=a
        for j in range(k,len(nums)):
            a+=nums[j]
            a-=nums[i]
            i+=1
            if a>b:
                b=a
        return b/k