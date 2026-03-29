class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0,0] + nums
        prev1, prev2 = 0,0
        curr = 0
        for i in range(2, len(nums)):

            curr = max(prev1, prev2 + nums[i]) ## max(9, 11) -> 11
            prev2, prev1 = prev1, curr
            
            print(f"Prev1: {prev1}, Prev2: {prev2}, house: {nums[i]}, max: {curr} ")

        return curr