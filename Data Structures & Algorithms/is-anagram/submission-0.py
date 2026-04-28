class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = set()
        char_t = set()
        
        for ch in s:
            char_s.add(ch)
        for ch in t:
            char_t.add(ch)
        
        if char_s == char_t:
            return True

        return False