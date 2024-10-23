class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        length = len(s1) 
        h1 = [] # create heaps for string character ascii values
        h2 = []
        for i in range(length): # fill heaps with ascii values
            heapq.heappush(h1, ord(s1[i]))
            heapq.heappush(h2, ord(s2[i]))
        greater = None
        index = 0
        while not greater: # pop from each heap until one of the values is greater than the other
            if index == length: return true # if the sorted permutations are equal return true
            c1 = heapq.heappop(h1)
            c2 = heapq.heappop(h2)
            if c1 > c2: greater = 1
            elif c2 > c1: greater = 2
            index += 1
        def check(greater_heap, lessor_heap): # continue popping from heaps and comparing ascii values
            for i in range(index, length):
                greater_char = heapq.heappop(greater_heap)
                lessor_char = heapq.heappop(lessor_heap)
                if greater_char < lessor_char: return False # return false when a greater_char value is less than a lessor_char value
            return True # return true once the heaps are empty
        if greater == 1: return check(h1, h2)
        elif greater == 2: return check(h2, h1) 