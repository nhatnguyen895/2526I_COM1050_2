class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a={}
        Max=0
        i=0
        for j in range(len(s)):
            if s[j] in a and a[s[j]]>=i:
                i=a[s[j]]+1
            a[s[j]]=j
            if Max<j-i+1:
                Max=j-i+1
        return Max