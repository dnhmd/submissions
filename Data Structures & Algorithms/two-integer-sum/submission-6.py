class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            if target - num in store:
                return [store[target - num], i]
            store[num] = i
        return []
