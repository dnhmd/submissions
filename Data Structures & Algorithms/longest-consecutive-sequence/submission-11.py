class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums.sort()
        i, j = 0, 1
        count = 1
        maximum = count
        while j < len(nums):
            if nums[j] - nums[i] == 1:
                count += 1
            elif nums[j] - nums[i] > 1:
                count = 1
            else:
                i += 1
                j += 1
                continue
            i += 1
            j += 1
            if count > maximum:
                maximum = count

        return maximum

# 2, 3, 4, 4, 5, 10, 20