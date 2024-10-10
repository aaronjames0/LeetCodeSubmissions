class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_r = [0]*len(nums)
        i = len(nums)-1
        prev_max = 0
        for n in nums[::-1]:
            max_r[i] = max(n,prev_max)
            prev_max = max_r[i]
            i=i-1
        l = 0
        Max = 0
        for r in range(len(nums)):
            while nums[l]>max_r[r]:
                l=l+1
            Max = max(Max,r-l)
        return Max