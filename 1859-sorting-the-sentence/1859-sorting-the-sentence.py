class Solution:
    def sortSentence(self, s: str) -> str:
        l = []
        
        for i in s.split(' '):
            l.append((i[-1],i[:-1]))
            
        l.sort()
        return (' '.join(word[1] for word in l))
        
        