class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = 2**maximumBit - 1 # Get the maximum value for maximumBit number of bits
        total = 0 # Initialize the running total
        res = [] # Initialize the res list
        for num in nums: # Iterate through nums
            total ^= num # XOR the next number into the total
            res.append(max_val ^ total) # Append the total XOR'd with the maximum value to get k
        return res[::-1] # Return res reversed