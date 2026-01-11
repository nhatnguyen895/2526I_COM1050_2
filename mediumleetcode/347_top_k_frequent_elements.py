class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        bucket=[]
        for i in nums:
            if i in count:
                count[i]+=1
            elif i not in count:
                count[i]=1
        for i in range(len(nums)+1):
            bucket.append([])
        for i in count:
            bucket[count[i]].append(i)
        ans=[]
        i=len(bucket)-1
        while len(ans)<k:
            for j in range(len(bucket[i])):
                if len(ans)<k:
                    ans.append(bucket[i][j])
            i-=1
        return ans