class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0 
        for i in nums: max_or |= i # find the maximum possible value by performing an or on all list elements
        @cache
        def helper(i, total):
            # when i is equal to len(nums), we have reached the end of that subset, compare total to max_or and return 1 to add the subset to our answer
            if i == len(nums): return 1 if total == max_or else 0
            # when a subset is still gathering values, call the helper function twice
            # one to include the value of nums[i] in the current or total, and one to ignore it
            # this will insure that we check the total value for all possible subsets
            return helper(i + 1, total | nums[i]) + helper(i + 1, total)
        # return helper(0, 0) to start with at nums[0] with a total of 0
        return helper(0, 0)