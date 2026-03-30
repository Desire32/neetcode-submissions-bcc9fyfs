class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) == len(s) and t != s:
            return ""
        if t.isupper() and s.islower():
            return ""
        if s == t:
            return t
                
        need, have = dict(), dict()
        formed, required = 0 , 0
        min_len = float("inf")
        res_L, res_R = 0, 0

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        for x in need.values():
            required += x
        print(need, required)
        
        L = 0
        for R in range(len(s)):
            have[s[R]] = have.get(s[R], 0) + 1

            if s[R] in need and have[s[R]] == need[s[R]]:
                formed += 1

            while formed == required: # valid window
                # update window first
                if R - L + 1 < min_len:
                    min_len = R - L + 1
                    res_L, res_R = L, R

                have[s[L]] -= 1
                if s[L] in need and have[s[L]] < need[s[L]]:
                    formed -= 1
                L += 1

        return s[L:R]