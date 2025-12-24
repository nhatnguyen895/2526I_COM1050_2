class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       i=m-1
       j=n-1
       a=m+n-1
       while i>=0 and j>=0:
        if nums1[i]>nums2[j]:
            nums1[a]=nums1[i]
            i-=1
            a-=1
        else:
            nums1[a]=nums2[j]
            j-=1
            a-=1
       nums1[:j+1]=nums2[:j+1]