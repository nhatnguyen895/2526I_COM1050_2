class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            a[nums[i]]=[i,0]
        for i in range(len(nums)):
            a[nums[i]][1]+=1
        for i in nums:
            if target - i in a and a[i]!=a[target-i]:
                return [a[i][0],a[target-i][0]]
            elif 2*i==target and a[i][1]>=2:
                c=[]
                for k in range(len(nums)):
                    if nums[k]==i:
                        c.append(k)
                return [c[0],c[1]]