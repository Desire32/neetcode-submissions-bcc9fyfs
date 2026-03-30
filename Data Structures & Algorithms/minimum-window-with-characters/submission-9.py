class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t:
            return t
                
        need, have = dict(), dict()
        min_len = float("inf")
        res_L, res_R = 0, 0

        for ch in t:
            need[ch] = need.get(ch, 0) + 1
            
        formed, required = 0 , len(need)
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
                    print(f"res_L, res_R: {res_L, res_R}")

                have[s[L]] -= 1
                if s[L] in need and have[s[L]] < need[s[L]]:
                    formed -= 1
                L += 1

        return s[res_L:res_R + 1] if min_len != float('inf') else ""