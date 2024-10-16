class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        white = 0
        for ball in s:
            if ball == "0": res += white # upon reaching a black ball, it will require white number of swaps to reach its proper index
            else: white += 1 # increment the white counter when a white ball is reached
        return res