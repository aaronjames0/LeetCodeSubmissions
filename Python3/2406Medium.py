class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0]) # sort intervals into ascending order based on starting value
        ends = [] # heap of current largest ending interval per group, length will be total groups of intervals
        for interval in intervals:
            start, end  = interval
            if ends and start > ends[0]: # current interval can be added to group with smallest ending value
                heapq.heappop(ends) # remove old ending value
            heapq.heappush(ends, end) # add new ending value
        return len(ends) # return length of resulting heap