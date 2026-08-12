class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        value = [[] for _ in range(len(nums) + 1)]
        for num, cnt in freq.items():
            value[cnt].append(num)
        
        res = []
        for i in range(len(value) - 1, 0, -1):
            for num in value[i]:
                res.append(num)
                if len(res) == k:
                    return res