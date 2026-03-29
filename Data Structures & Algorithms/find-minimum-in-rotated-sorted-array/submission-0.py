class Solution:
    def findMin(self, nums: List[int]) -> int:
     # оказывается тот же самый принцип только мы не проходим весь а просто обрубаем кусок сразу!     
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[left] == nums[right]:
                return nums[left]

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return -1

            