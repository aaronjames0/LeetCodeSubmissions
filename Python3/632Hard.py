class Solution:
    def smallestRange(self, nums):
        curr_vals = [] # create a heap to store the current values we're observing
        max_v = float('-inf') # create a max value tracker
        
        for i in range(len(nums)): # populate the current values and track the max value
            heapq.heappush(curr_vals, (nums[i][0], i, 0)) # begin by looking at the first value from each list
            max_v = max(max_v, nums[i][0]) # update the max value as each value is added
        
        low, high = -float('inf'), float('inf') # create values for the low and high halves of the smallest range
        
        while curr_vals: # begin moving through the values and looking for the smallest range
            min_v, list_i, val_i = heapq.heappop(curr_vals) # pop the smallest value from the heap along with its location
            if max_v - min_v < high - low: low, high = min_v, max_v # update low and high when a smaller range is found
            if val_i + 1 < len(nums[list_i]):
                next_v = nums[list_i][val_i + 1] # get the next value from min_v's heap if it exists
                heapq.heappush(curr_vals, (next_v, list_i, val_i + 1)) # push it to the current values
                max_v = max(max_v, next_v) # updates the max value if the next is the biggest of our current values
            else: break # if the previous min value was the last of its list, we are ready to return the smallest range
        
        return [low, high]