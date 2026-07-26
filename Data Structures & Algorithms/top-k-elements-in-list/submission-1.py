class Solution:
    # Min Heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a frequency map
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # build an empty min-heap
        heap = []

        # for each number in the frequency map
        for num in count.keys():
            # push (frquency, number) unto the heap
            heapq.heappush(heap, (count[num], num))
            # if the heap size becomes greater than k, pop once to remove the smallest frequency
            if len(heap) > k:
                heapq.heappop(heap)
        
        # after processing, the heap contains the k most frequent elements

        # pop all elements from the heap and collect their numbers into the result list
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        # return result
        return res
        