class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0] * 24 # Create a list to represent the total number of bits for every possible position, max val is 10,000,000, so 24 bits are needed
        for num in candidates: # Begin iterating through the candidates
            position = 0 # Position will represent the index of the bit
            for bit in "{0:b}".format(num)[::-1]: # Convert the candidate to a binary string and traverse reversely
                if bit == "1": bits[position] += 1 # Increment the bit counter if the current bit is 1
                position += 1 # Increment the bit position index
        return max(bits) # Return the max value seen in the bits array