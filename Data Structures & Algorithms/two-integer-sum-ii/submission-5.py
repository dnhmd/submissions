class Solution:
    # Two Pointers (O(n), O(1))
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            tmp = numbers[i] + numbers[j]
            if tmp < target:
                i += 1
            elif tmp > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return []