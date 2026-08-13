class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums.sort()
        longest = count = 1
        i, j = 0, 1

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
            longest = max(count, longest)
        
        return longest