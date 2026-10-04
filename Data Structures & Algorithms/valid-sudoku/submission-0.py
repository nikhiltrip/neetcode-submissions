class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                
                checks = (
                    ("row", r, value),
                    ("column", c, value),
                    ("box", r // 3, c // 3, value)
                )

                for check in checks:
                    if check in seen:
                        return False
                    seen.add(check)
        
        return True