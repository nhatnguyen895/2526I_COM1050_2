class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a=strs[0]
        b=strs[-1]
        i=0
        while i<len(a) and i<len(b):
            if a[i]==b[i]:
                i+=1
            else:
                break
        return a[:i]