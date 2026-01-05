class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                break
            elif nums[mid]<target:
                i=mid+1
            elif nums[mid]>target:
                j=mid-1
        if len(nums)==0:
            return [-1,-1]
        elif nums[mid]!=target:
            return [-1,-1]
        i=0
        j=mid
        while i<j:
            midleft=(i+j)//2
            if nums[midleft]!=target:
                i=midleft+1
            elif nums[midleft]==target:
                j=midleft
        left=j
        i=mid
        j=len(nums)-1
        while i<j:
            midright=(i+j)//2
            if (i+j)/2>midright:
                midright+=1
            if nums[midright]!=target:
                j=midright-1
            elif nums[midright]==target:
                i=midright
        right=i
        return [left,right]
        
                
