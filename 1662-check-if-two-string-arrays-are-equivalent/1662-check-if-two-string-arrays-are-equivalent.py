class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ''.join([i.lower() for i in word1])
        s2 = ''.join([i.lower() for i in word2])
        
        return (s1==s2)
        