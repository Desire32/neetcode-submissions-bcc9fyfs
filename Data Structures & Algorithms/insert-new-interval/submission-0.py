class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = 0, 0
        i = 0
        # 1. left border check
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
            start = i
            print(f"Start pos: {start}")
        # 2. right border check
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            i += 1
            end = i - 1 # last intersection
            print(f"End pos: {end}")
        # 3. intersection
        if i > start:
            newInterval[0] = min(newInterval[0], intervals[start][0])
            newInterval[1] = max(newInterval[1], intervals[end][1])

        return intervals[:start] + [newInterval] + intervals[i:]
