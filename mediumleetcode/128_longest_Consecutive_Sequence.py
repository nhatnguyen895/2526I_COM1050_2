class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       used={}
       a={}
       for i in nums:
        a[i]=0
       Length=0
       for i in nums:
        if i not in used:
            used[i]=0
            Len=1
            b=i
            while True:
                if i+1 in a:
                    i+=1
                    used[i]=0
                    Len+=1
                elif b-1 in a:
                    b-=1
                    used[b]=0
                    Len+=1
                else:
                    break
            if Length<Len:
                Length=Len
       return Length