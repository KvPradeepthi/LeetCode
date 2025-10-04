class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        # Step 1: Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            
            if current[0] <= last[1]:
                # Overlapping intervals → merge
                last[1] = max(last[1], current[1])
            else:
                # No overlap → add current interval
                merged.append(current)
        
        return merged
