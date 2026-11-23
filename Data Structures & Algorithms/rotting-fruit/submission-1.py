from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        # enqueue every rotten fruit on our queue
        # if the queue is empty -> -1 
        # if in every direction of a rotten_fruit we have a fresh fruit -> pass it onto a rotten fruit
        # also we need to enqueue the new rottenFruit 
        rows, cols = len(grid), len(grid[0])
        ROTTEN = 2
        FRESH = 1
        nb_fresh_cell = 0
        for x in range (rows):
            for y in range(cols):
                if grid[x][y] == ROTTEN:
                    queue.append((x,y))
                if grid[x][y] == FRESH:
                    nb_fresh_cell += 1
        # if len(queue)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        output = 0
        while queue:
            swap = False
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    node_x, node_y = dx + x, dy + y 
                    if 0 <= node_x < rows and 0 <= node_y < cols and grid[node_x][node_y] == FRESH:
                        nb_fresh_cell -= 1
                        grid[node_x][node_y] = ROTTEN
                        queue.append((node_x, node_y))
                        swap = True
            if swap:
                output += 1
        if nb_fresh_cell != 0:
            return -1
        return output 
        