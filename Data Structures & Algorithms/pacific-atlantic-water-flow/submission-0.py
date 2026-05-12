from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # we have two oceans, therefore we need two queues
        pq, aq = deque(), deque()
        pq_visited, aq_visited = set(), set()

        for i in range(rows):
            # pacific ocean
            pq.append((i, 0))
            pq_visited.add((i, 0))

            # atlantic ocean
            aq.append((i, cols - 1))
            aq_visited.add((i, cols - 1))
        
        for j in range(cols):
            pq.append((0,j))
            pq_visited.add((0,j))

            aq.append((rows - 1, j))
            aq_visited.add((rows - 1, j))
        
        def bfs(q, visited):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            print(visited)

        bfs(pq, pq_visited)
        bfs(aq, aq_visited)

        return [[r,c] for r, c in pq_visited & aq_visited]


                
