class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        store = [[] for _ in range(len(nums) + 1)]
        for num, cnt in freq.items():
            store[cnt].append(num)
        
        res = []
        for i in range(len(store) - 1 , 0, -1):
            for num in store[i]:
                res.append(num)
                if len(res) == k:
                    return res