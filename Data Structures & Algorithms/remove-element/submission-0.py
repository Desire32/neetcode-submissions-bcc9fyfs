class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        to_write = 0

        for to_read in range(len(nums)):
            if nums[to_read] != val:
                nums[to_write] = nums[to_read]
                to_write += 1

        for right in range(1, to_write):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        print(nums[:left + 1])
        return left + 1
