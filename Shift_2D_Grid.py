class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for g_lop in range(k):
            for n in range(len(grid)-1):
                grid[n+1].insert(0,grid[n].pop())
            grid[0].insert(0,grid[-1].pop(-1))
        return grid
