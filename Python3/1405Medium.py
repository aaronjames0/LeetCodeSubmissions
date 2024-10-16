class Solution:
    def get_chunks(self, count, breaks): # create a list of the chunk sizes of the most abundant character
        chunk, chunks = 0, []
        while breaks >= 0 and count > 0:
            if chunk == 2: # when a chunk has reached the size limit
                chunks.append(chunk) # append it to the list
                chunk, breaks = 0, breaks - 1 # reset chunk, decrement number of possible breaks
            else: # a chunk can still be added to
                chunk, count = chunk + 1, count - 1 # add to the chunk, decrement count of most abundant character 
                if count == 0: chunks.append(chunk) # append the current chunk if that was the last of the most abundant character
        return chunks

    def get_most(self, a, b, c): # returns the string value of the most abundant character, or the empty string if all are equal
        if (a >= b and a > c) or (a > b and a >= c): return "a" 
        if (b >= a and b > c) or (b > a and b >= c): return "b"
        if c > a and c > b: return "c"
        if a == b == c: return ""

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        chars = {"a": a, "b": b, "c": c} # create map of character to their values
        most = self.get_most(a,b,c) # get the most abundant character
        if most == "": return (("a"+"b"+"c")*a) # if all characters are equal, return the string "abc" * a
        breaks = 0 # total up the highest possible count of breaks between substrings of the most abundant character
        for char in ["a","b","c"]:
            if char != most: breaks += chars[char]
        chunks = self.get_chunks(chars[most], breaks) # get the chunk sizes of the most abundant character
        gap_count = len(chunks) # count the gaps/chunks
        for i in range(gap_count): chunks[i] = most * chunks[i] # replace the chunk lengths with strings of the most abundant character
        chars[most], i = 0, 0 # remove the most abundant character from the map
        gaps = [""] * gap_count # create a list of the gaps to go between chunks
        while (chars["a"] > 0) or (chars["b"] > 0) or (chars["c"] > 0): # while there are unused characters
            if i == gap_count: i = 0 # reset the gap index
            if chars["a"] > 0: gaps[i], chars["a"], i = gaps[i] + "a", chars["a"] - 1, i + 1 # append an "a" to the current gap, decrement map value, and increment index  
            elif chars["b"] > 0: gaps[i], chars["b"], i = gaps[i] + "b", chars["b"] - 1, i + 1 # append an "b" to the current gap, decrement map value, and increment index  
            elif chars["c"] > 0: gaps[i], chars["c"], i = gaps[i] + "c", chars["c"] - 1, i + 1 # append an "c" to the current gap, decrement map value, and increment index  
        for i in range(gap_count): res += chunks[i] + gaps[i] # stitch together the chunks and gaps
        return res