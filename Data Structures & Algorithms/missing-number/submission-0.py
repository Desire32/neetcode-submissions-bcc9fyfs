class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n
        for i in range(0, n):
            result ^= i # result ^ i (0, 0) -> 0
            print(f"first XOR: {result}")
            result ^= nums[i] # result ^ nums[i] (0, 1) -> 1
            print(f"second XOR: {result}")
        return result