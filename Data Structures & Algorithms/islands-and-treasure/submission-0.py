from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for direction in directions:
                new_r, new_c = r + direction[0], c + direction[1]
                if new_r >= 0 and new_r <= len(grid) - 1 and new_c >= 0 and new_c <= len(grid[0]) - 1 and grid[new_r][new_c] == 2**31 - 1:
                    grid[new_r][new_c] = grid[r][c] + 1
                    q.append((new_r, new_c))
