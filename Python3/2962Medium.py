class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        max_val = 0
        indices = [] # save the indices of the max value elements
        l1 = 0 # track length of indices array/occurences of max val
        for i in range(len(nums)):
            if nums[i] > max_val: # reset tracking
                max_val = nums[i]
                indices = [i]
                l1 = 1
            elif nums[i] == max_val: # append index and increment l1
                indices.append(i)
                l1 += 1
        if l1 < k: return 0

        l2 = len(nums) # get the length of nums, right bound for sub arrays
        left_limit = -1 # set the left bound for sub arrays

        for i in range(l1 - (k - 1)): 
            left = indices[i] # rightmost left index of subarray with this index as its first occurence of max val
            right = indices[i + (k - 1)] # leftmost right index of subarray with this index as its kth occurence of max val
            res += (left - left_limit) * (l2 - right) # formula for number of subarrays with indices[i] as its first occurence
            left_limit = left # update left limit
        
        return res