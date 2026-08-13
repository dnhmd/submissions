class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        i, j = 0, 1
        count = maximum = 1

        nums.sort()

        while j < len(nums):
            if nums[j] - nums[i] > 1:
                count = 1
            elif nums[j] - nums[i] == 1:
                count += 1
            else:
                i += 1
                j += 1
                continue
            i += 1
            j += 1
            maximum = max(count, maximum)
        
        return maximum