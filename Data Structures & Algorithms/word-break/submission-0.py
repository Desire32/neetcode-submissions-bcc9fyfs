class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        n = len(s) + 1 # + 1 because we must count first (0) pos
        dp = [False for _ in range(n)]
        dp[0] = True # first pos always built 
        
        for i in range(1, n): # can we built a string up to here
            for j in range(0, i): # was j built already in dp[]
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
            
        return dp[-1] # return the last element