class Solution:
    def maxDepth(self, s: str) -> int:
        depth, vps = 0, 0
        
        for i in s:
            if i=='(':
                vps+=1
            elif i==')':
                vps -=1
            depth = max(depth, vps)
        return depth

        