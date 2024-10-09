class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        p = []
        c = 0
        for char in s:
            if char == "(": p.append(char)
            elif len(p) != 0: p.pop()
            else: c += 1
        return len(p) + c