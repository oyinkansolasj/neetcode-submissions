class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMap = {}
        for s in strs: 
            newStr = "".join(sorted(s))
            if newStr not in prevMap: 
                prevMap[newStr] = []
            prevMap[newStr].append(s)
        return list(prevMap.values())
        