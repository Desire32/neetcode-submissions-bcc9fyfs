class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # Test cases we know for sure:
        # 1. dp[i][i] = True
        # 2. dp[i][i+1] = s[i][s+1]

        start, max_len = 0, 1

        for length in range(1, len(s) + 1): # 1, because a minimal substring is one
            '''
                `j` must not leave a string, so `j <= len(s) - 1`:
                i + length - 1 <= len(s) - 1
                i <= len(s) - length
            '''
            for i in range(0, len(s) - length + 1):
                j = i + length - 1 # this is the end
                if length == 1: dp[i][j] = True
                if length == 2 and s[i] == s[j]: dp[i][j] = True
                if length >= 3 and s[i] == s[j] and dp[i+1][j-1]: dp[i][j] = True
                '''
                j - i + 1 = the length of the palindrome we just saw
                max_len = the max length of the palindrome we have seen before
                if current is bigger than the previous one -> update
                '''
                if j - i + 1 > max_len and dp[i][j] == True: # эта хуйня изобретена укропами
                    max_len = j - i + 1
                    start = i

        return s[start:start + max_len] # cut substring we need


               