class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.explore(grid, r, c, visited) is True:
                    count += 1
        return count
    def explore(self, grid, r , c , visited):
        row_bounds = 0 <= r < len(grid)
        col_bounds = 0 <= c < len(grid[0])

        if not row_bounds or not col_bounds:
            return False
        if grid[r][c] == '0':
            return False
        if (r, c) in visited:
            return False
        visited.add((r , c))
        self.explore(grid, r + 1 , c , visited)
        self.explore(grid, r - 1 , c , visited)
        self.explore(grid, r , c + 1 , visited)
        self.explore(grid, r , c - 1 , visited)   
        return True                         



