class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        # greedy algorithm
        sum_area = 0
        for i in range(0, len(heights) - 1):
            cnt = heights[i]
            sum_area = max(sum_area, cnt)
            if sum_area >= heights[i+1]:
                left = i
                break
        print(f"Left border: {left}")

        width = right - left
        height = min(heights[left], heights[right])
        
        return width * height