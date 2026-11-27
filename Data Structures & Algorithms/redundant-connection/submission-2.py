from collections import defaultdict, deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Pour n nœuds numérotés de 1 à n
        parent = list(range(1000 + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # Déjà connectés -> cycle !
            parent[rootY] = rootX
            return True
        for [x, y] in edges:
            if union(x, y) == False:
                return [x, y]
        return []
            