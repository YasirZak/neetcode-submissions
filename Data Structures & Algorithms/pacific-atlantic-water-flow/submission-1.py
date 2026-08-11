from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r: int, c: int, reachable: set):
            reachable.add((r, c))
            # Check all 4 adjacent directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # Check boundaries and unvisited status
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable:
                    # Water flows downhill (or equal height), so traveling 
                    # backwards from the ocean means moving uphill (heights[nr][nc] >= heights[r][c])
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, reachable)

        # 1. Start DFS from Pacific borders (Top row & Left column)
        # 2. Start DFS from Atlantic borders (Bottom row & Right column)
        for r in range(rows):
            dfs(r, 0, pacific_reachable)          # Pacific (Left)
            dfs(r, cols - 1, atlantic_reachable)  # Atlantic (Right)

        for c in range(cols):
            dfs(0, c, pacific_reachable)          # Pacific (Top)
            dfs(rows - 1, c, atlantic_reachable)  # Atlantic (Bottom)

        # The result is the intersection of cells reachable by both oceans
        return list(map(list, pacific_reachable & atlantic_reachable))