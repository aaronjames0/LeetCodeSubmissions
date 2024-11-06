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
            while heap: # While nums exist in the heap
                num = heapq.heappop(heap) # Get the next num
                if prev and prev > num: return False # Return False if prev has been set and it is greater than the next num
                prev = num # Update the prev value
        return True # If the code has reached this line, sorting the list is possible