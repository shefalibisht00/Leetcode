class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):  return False
        sMap, tMap = [0]*26, [0]*26
        
        # Two concepts: Sliding Window and HashMap
        for i in range(len(s)):
            sMap[ord(s[i]) - ord('a')] += 1
            tMap[ord(t[i]) - ord('a')] += 1
            
        return (sMap==tMap)
        
        