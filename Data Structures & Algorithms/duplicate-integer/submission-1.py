class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = set()

        for n in nums:
            if n in k:
                return True
            k.add(n)

        return False