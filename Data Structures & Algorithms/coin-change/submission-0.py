class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 : return 0

        n = amount + 1
        dp = [float('inf') for _ in range(n)]
        dp[0] = 0

        # O(n*t)
        for i in range(1, n): # 1 because we hape dp[0] = 0
            for c in coins: # for each sum we ask, what coin (c) can be last?
                if i - c >= 0: dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1