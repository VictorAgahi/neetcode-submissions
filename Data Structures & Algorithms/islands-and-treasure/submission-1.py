from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    queue.append((x, y))
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < rows and 0 <= ny < cols and INF == grid[nx][ny]:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))
