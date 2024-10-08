# Minimum Number of Swaps to Make the String Balanced
class Solution:    
    def minSwaps(self, s: str) -> int:
        swaps = 0 # set swap counter to 0, we will return this
        o1 = 0 # open brackets seen by i1
        c1 = 0 # closed brackets seen by i1
        o2 = 0 # open brackets seen by i2
        c2 = 0 # closed brackets seen by i2
        i1 = 0 # set i1 to first index of s
        i2 = len(s) - 1 # set i2 to last index of s
        while i1 < i2: # while indices have not overlapped
            while i1 < i2 and c1 <= o1: #run until overlapping i2 or finding an extra closing bracket
                if s[i1] == "]": c1 += 1 # increment closing bracket
                else: o1 += 1 # increment opening bracket
                i1 += 1 # increment index 1
            while i2 > i1 and o2 <= c2: # run until overlapping i1 or finding an extra opening bracket
                if s[i2] == "[": o2 +=1 # increment opening bracket
                else: c2 += 1 # increment closing bracket
                i2 -=1 # decrement index 2
            if c1 > o1: # if index 1 has seen an extra closing bracket
                o1 += 1 # adjust counters for implied swap
                c1 -= 1 # adjust counters for implied swap
                o2 -= 1 # adjust counters for implied swap
                c2 += 1 # adjust counters for implied swap
                swaps += 1 #increment swap counter
        return swaps