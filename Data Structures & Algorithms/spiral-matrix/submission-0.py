# Notes taken from: [https://www.geeksforgeeks.org/dsa/print-a-given-matrix-in-spiral-form/]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1. get mxn sizes
        m = len(matrix)
        n = len(matrix[0])

        # 2. direction arrays and init pos
        r, c = 0, 0
        dr = [0, 1, 0, -1] # right and left, direction row
        dc = [1, 0, -1, 0] # down and up, direction column

        idx = 0 # represents the init pos, which is right

        # 3. output and visited pos
        output = []
        visited = [[False] * n for _ in range(m)]

        for _ in range(m*n):
            output.append(matrix[r][c])
            visited[r][c] = True

            # calculate the next coordinate
            newR, newC = r + dr[idx], c + dc[idx]

            if 0 <= newR < m and 0 <= newC < n and not visited[newR][newC]: # checking in case we visited it and within bounds
                r, c = newR, newC
            else:
                idx = (idx + 1) % 4 # [% n] is being used each time we wish to get an infinite loop

                r += dr[idx] # new row direction
                c += dc[idx] # new col direction
        return output









