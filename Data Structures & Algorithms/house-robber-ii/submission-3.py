class Solution:
    def _robber(self, nums: List[int]) -> int:
        prev1, prev2 = 0,0
        curr = 0
        for i in range(0, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            print(f"prev2: {prev2}, prev1: {prev1}, curr: {curr}")
            prev2, prev1 = prev1, curr
        return curr
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        n = len(nums)

        # 1. we decide that we rob the first house
        opt1 = self._robber(nums[0:n-1])
        # 2. we decide that we rob the last house
        opt2 = self._robber(nums[1:n])

        return max(opt1, opt2)

