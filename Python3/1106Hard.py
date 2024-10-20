class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        length = len(expression) # get the length of the expression

        def helper(i, operation): # recursive function, take in index and the current operation, if any
            bools = [] # create a list of boolean values to perform the operation on
            char = expression[i] 

            while char != ")": # iterate through the characters until a closing parentheses is reached
                if char == ",": # continue to next iteration when a , is seen
                    i += 1
                    char = expression[i]

                elif char == "!" or char == "&" or char == "|": # create a recursive call when an operation character is found
                    op = helper(i + 2, char) # call the operation recursively, increment the index over the opening parentheses
                    bools.append(op[0]) # append the resulting boolean value
                    i = op[1] # update the index
                    if i < length - 1: # get the next character if one exists
                        i += 1
                        char = expression[i]
                    else: break # break the loop if the index is at the last character

                else: # must be a boolean value, append it to bools and get the next character
                    if char == "f": bools.append(False)
                    else: bools.append(True)
                    i += 1
                    char = expression[i]

            if not operation: return bools[0] # return the final result to our initial function call

            elif operation == "!": return [not bools[0], i] # return the not value to the recursive call

            elif operation == "&": # iterate boolean values and return the & value to the recursive call
                for b in bools:
                    if not b: return [False, i] # result is False if a False value exists in bools
                return [True, i]
            
            elif operation == "|": # iterate boolean values and return the | value to the recursive call
                for b in bools:
                    if b: return [True, i] # result is True if a True value exists in bools
                return [False, i]
            
        return helper(0, None) # return a call to the helper function starting at index 0 and having a null operation