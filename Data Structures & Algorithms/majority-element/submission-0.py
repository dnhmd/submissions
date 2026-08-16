class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = {}
        major = 0
        for num in nums:
            store[num] = store.get(num, 0) + 1
        
        for num, i in store.items():
            if i > len(nums) / 2:
                major = num
        
        return major