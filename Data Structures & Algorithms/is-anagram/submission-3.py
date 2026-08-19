class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
            
        map_s = {}
        map_t = {}

        for c in s: 
            map_s[c] = map_s.get(c, 0) + 1 

        for c in t: 
            map_t[c] = map_t.get(c, 0) + 1 

        for key in map_s: 
            if map_s[key] != map_t.get(key, 0): 
                return False
        return True