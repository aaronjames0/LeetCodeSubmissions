class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        length = len(num)
        heap = []
        for i in range(length): heapq.heappush(heap,int(num[i]) * -1)
        for i in range(length):
            val = heapq.heappop(heap) * -1
            if int(num[i]) != val:
                for j in range(i + 1,length)[::-1]:
                    if int(num[j]) == val:
                        num = num[:i] + str(val) + num[i + 1:j] + num[i] + num[j + 1:]
                        break
                break
        return int(num)