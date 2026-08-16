class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if not num - 1 in numSet:
                count = 1
                while (num + count) in numSet:
                    count += 1
                longest = max(count, longest)
        
        return longest