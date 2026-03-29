# Solved using BFS Approach
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    counter += 1

                    q = deque() # we initialize queue in the loop
                    q.append((r,c))
                    print(f"Queue: {q}")
                    grid[r][c] == '0'

                    while q:
                        row, col = q.popleft() # FIFO

                        for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = row + dr, col + dc
                            # border check
                            print(f"New row, new col: {nr, nc}")
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                q.append((nr,nc))
        return counter