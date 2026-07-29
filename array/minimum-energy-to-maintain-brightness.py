class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()
        merged=0
        start,end=intervals[0]
        for s,e in intervals[1:]:
            if s<=end+1:
                end=max(end,e)
            else:
                merged+=end-start+1
                start,end=s,e
        merged+=end-start+1
        nav=(n,brightness,intervals)
        bulbs=(brightness+2)//3
        return merged*bulbs