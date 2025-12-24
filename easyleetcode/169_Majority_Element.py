class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        a=None 
        for i in nums:
            if count==0:
                a=i
            if a==i:
                count+=1
            else:
                count-=1
        return a
