class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        heap = [] # Initialize a heap to sort sub arrays of equal set bit counts
        index = 0 # Initialize an index int to traverse nums
        length = len(nums) # Get the length of nums
        prev = None # Initialize a null int for the previous num value
        while index < length: # Iterate through nums
            first = nums[index].bit_count() # Get the set bit count of the next num
            while index < length and first == nums[index].bit_count(): # While the index is valid and the current num's bit count matches
                heapq.heappush(heap, nums[index]) # Push the num to the heap
                index += 1 # Increment the index
            num = heapq.heappop(heap) # Get the minimum value of the heap
            if prev and prev > num: return False # Return False if prev has been set and it is greater than the next num
            while heap: num = heapq.heappop(heap) # Empty the heap, keeping track of the last value
            prev = num # Update the previous value with num
        return True # If the code has reached this line, sorting the list is possible