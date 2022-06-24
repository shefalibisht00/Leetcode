class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        charSet = set()
        
        for right in range(len(s)):
            # Remove until all duplicates are removed from set
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            maxLength = max(maxLength, right-left+1)
        
        return(maxLength)

        