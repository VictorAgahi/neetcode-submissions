from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # [[0,1],[1,2],[3,4]]
        adj = defaultdict(list)
        for [x, y] in edges:
            adj[x].append(y)
            adj[y].append(x)
        queue = deque()
        component = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                queue.append(i)
                visited.add(i)
                component += 1

            while queue:
                current_node = queue.popleft()
            
                for node in adj[current_node]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)
        return component
        