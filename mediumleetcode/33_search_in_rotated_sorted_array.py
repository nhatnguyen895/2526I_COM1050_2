class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<j and nums[i]>nums[j]:
            mid=(i+j)//2
            if j-i==1 and nums[i]>nums[j]:
                break
            elif nums[i]<nums[mid]:
                i=mid
            elif nums[j]>nums[mid]:
                j=mid
        def binary_search(i,j,nums,target):
            while i<=j:
                mid=(i+j)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    i=mid+1
                elif nums[mid]>target:
                    j=mid-1
            return -1
        if i==0 and j==len(nums)-1 and nums[i]<nums[j]:
            return binary_search(i,j,nums,target)
        a=binary_search(0,i,nums,target)
        b=binary_search(j,len(nums)-1,nums,target)
        if a==-1 and b==-1:
            return a
        elif a!=-1:
            return a
        elif b!=-1:
            return b
