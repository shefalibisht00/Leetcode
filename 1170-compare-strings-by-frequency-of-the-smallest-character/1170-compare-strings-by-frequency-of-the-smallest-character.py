from collections import Counter

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queries_d, words_d = dict(), dict()
        if len(queries)==0: return []
        #Create Freq map for queries
        for i in queries:
            l = list(i)
            l.sort()
            queries_d[i] = l.count(l[0])
            
        for i in words:
            l = list(i)
            l.sort()
            words_d[i] = l.count(l[0])
            
        cnt = 0
        out = []
        for i in queries:
            for j in words:
                if queries_d[i]<words_d[j]: cnt+=1
            out.append(cnt)
            cnt=0
        return(out)
            
            
            