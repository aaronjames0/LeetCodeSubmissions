class Solution:
    def compressedString(self, word: str) -> str:
        res = "" # Declare empty result strin
        length = len(word) # Get length of word
        i = 0 # Declare index int as 0
        while i < length:
            char = word[i] # Get the character at index i
            j = 1 # Declare the character count int as 1
            for k in range(i + 1, length): # Iterate from i + 1 onwards
                if word[k] == char: j += 1 # Increment j if the enxt character matches the character at i
                else: break
                if j == 9: break # stop the count if it reaches 9
            res += str(j) + char # Append the value of j and the character it is counting
            i += j # Increment i by j
        return res