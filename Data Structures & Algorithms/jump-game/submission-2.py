class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # for idx in range(len(nums)):
        #     print(idx)
        #     idx += nums[idx]

        #     if nums[idx] == 0 and nums[idx] != nums[-1]:
        #         return False
        # return True
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            print(f"Reach: {max_reach}, i: {i}")
        return True