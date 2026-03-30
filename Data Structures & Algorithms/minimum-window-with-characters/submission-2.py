class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) == len(s) and t != s:
            return ""
        if t.isupper() and s.islower():
            return ""
        unique_chars, store = set(), dict()
        n, window_len = len(s), len(t)
        result = ""

        # 1. Store all unique chars of t
        for ch in t:
            unique_chars.add(ch)

        # 2. Store positions of simillar chars    
        for i, ch in enumerate(s):
            if ch in unique_chars:
                store[ch] = i

        print(unique_chars)
        print(store)
        L, R = min(store.values()), max(store.values()) # left and right border of sliding window
        
        print(L , R)
        for i in range(L, R + 1):
            result += s[i]

        return result