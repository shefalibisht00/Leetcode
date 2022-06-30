class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        d = [int(token) for token in s.split(' ') if token.isdigit()]
        
        for i in range(len(d)-1):
            if d[i]>=d[i+1]:    return False
        return True
            
        