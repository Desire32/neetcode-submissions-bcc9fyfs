from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:  
        if not node:
            return None

        visited = {}

        visited = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            print(f"curr val: {curr.val}")
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])

        return visited[node]

        
