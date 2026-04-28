class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for idx in range(len(nums)):
            print(idx)
            idx += nums[idx]

            if nums[idx] == 0 and nums[idx] != nums[-1]:
                return False
        return True