class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        s1Count, s2Count = [0]*26, [0]*26
        out = [] 
        win = len(s1)
        if len(s2)<win: return out
        
        for i in range(win):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1   

        i = 0
          
        for right in range(len(s1), len(s2)):
            if s1Count==s2Count:
                out.append(i)
            # Decrement the value
            s2Count[ord(s2[i]) - ord('a')] -= 1 
            # Add next element
            s2Count[ord(s2[right]) - ord('a')] += 1
            i += 1
        if (s1Count==s2Count):
            out.append(i)
        return (out)
            
        