class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for i in strs:
            a[tuple(sorted(i))]=[]
        for i in strs:
            a[tuple(sorted(i))].append(i)
        return list(a.values())