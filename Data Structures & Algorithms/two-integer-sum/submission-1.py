class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            curr = target - n
            if curr in hm:
                return [hm[curr], i]
            hm[n] = i
