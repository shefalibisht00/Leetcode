class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by first key
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for start,end in intervals[1:]:
            lastEnd = result[-1][1]
            
            if lastEnd>=start:
                #merge
                result[-1][1] = max(lastEnd,end)
            else:
                result.append([start,end])
            
        return result
                
                
        