from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Graph = Valid Tree mean that 
        we have a root and every nodes of the tree cannot be link to the another node of a same level / above expect one 
        
        The idea could be to find the root first and by using bfs we can walk through the graph and note the level
        
        We need the check if the graph is connexe else -> false

        """
        length = len(edges)

        adj = defaultdict(list)
        for [x, y] in edges:
            adj[x].append(y)
            adj[y].append(x)

        queue = deque()
        queue.append((0, -1))
        seen = set()
        seen.add(0)

        while queue:
            curr_parent, prev_parent = queue.popleft()
            for node in adj[curr_parent]:
                if node == prev_parent:
                    continue
                if node in seen:
                    return False
                seen.add(node)
                queue.append((node, curr_parent))
        return len(seen) == n


        



        