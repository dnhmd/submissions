class Solution:
    # Sorting
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map to store frequency of each number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # build a list of [frequency, number] pairs from the map
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        
        # sort this list in ascending order based on frequency
        arr.sort()

        # empty result list
        res = []

        # stop when result contains k elements
        while len(res) < k:
            # repeatedly pop from the end of the sorted list and append the number to the result
            res.append(arr.pop()[1])
        
        #return result list
        return res