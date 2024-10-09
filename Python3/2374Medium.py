class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        size = len(edges)
        scores = [0] * size
        for i in range(size):
            scores[edges[i]] += i
        highest = 0
        index = 0
        for i in range(size):
            j = size - 1 - i
            if scores[j] >= highest:
                highest = scores[j]
                index = j
        return index