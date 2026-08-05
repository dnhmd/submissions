class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        count = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            store[num] = store.get(num, 0) + 1
        
        for num, cnt in store.items():
            count[cnt].append(num)
        
        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res