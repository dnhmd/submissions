class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        store = {}
        for i in range(len(s)):
            if s[i].lower() in store and store[s[i].lower()] != t[i].lower():
                return False
            if t[i].lower() in store.values() and s[i].lower() not in store:
                return False
            store[s[i].lower()] = t[i].lower()
        
        return True