class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            store = [0] * 26
            for c in s:
                store[ord(c) - ord('a')] += 1
            groups[tuple(store)].append(s)
        return list(groups.values())