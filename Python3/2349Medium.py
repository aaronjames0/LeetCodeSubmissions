class NumberContainers:

    def __init__(self):
        self.vm = {} # maps a value to a heap of its indices
        self.im = {} # maps an index to its current value

    def change(self, index: int, number: int) -> None:
        if number not in self.vm: self.vm[number] = [] # creates a mapping of a new number to an empty heap
        self.im[index] = number # update the index map with its new value
        heapq.heappush(self.vm[number], index) # pushes the assigned index to the values mapped heap

    def find(self, number: int) -> int:
        if number not in self.vm: return -1
        heap = self.vm[number]
        while heap: # get the number's heap and iterate through it
            index = heapq.heappop(heap) # remove the smallest index from the heap
            if self.im[index] == number: 
                heapq.heappush(heap, index) # re-insert the index into the heap if the number is still at that index
                return index
            
        return -1