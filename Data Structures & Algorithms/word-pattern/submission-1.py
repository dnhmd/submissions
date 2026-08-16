class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s + ' '
        words = []
        word = ''
        for c in s:
            if c == ' ':
                words.append(word)
                word = ''
                continue
            word += c
        
        if len(pattern) != len(words):
            return False
        
        store = {}
        for i in range(len(pattern)):
            if pattern[i] in store and store[pattern[i]] != words[i]:
                return False
            if words[i] in store.values() and pattern[i] not in store:
                return False
            store[pattern[i]] = words[i]
        
        return True