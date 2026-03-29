class Solution:
    # no comments...
    def _combinator(self, target, i , path, nums, result):
        if target == 0: 
            result.append(path.copy()) 
            return
        if target < 0: return

        for j in range(i, len(nums)):
            path.append(nums[j])
            self._combinator(target - nums[j], j, path, nums, result)
            path.remove(nums[j])


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, path = [], []
        self._combinator(target, 0, path, nums, result)
        return result
