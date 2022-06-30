class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = [0]*26, [0]*26
        win = len(s1)
        if len(s2)<win: return False
        
        for i in range(win):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1   

        i, right = 0, win-1
        
        if len(s2)==win: return (s1Count==s2Count)
        
        for right in range(len(s1), len(s2)):
            if s1Count==s2Count:
                return True
            else:
                # Decrement the value
                s2Count[ord(s2[i]) - ord('a')] -= 1 
                # Add next element
                s2Count[ord(s2[right]) - ord('a')] += 1
            i += 1
        return (s1Count==s2Count)
            
        
        
        
        