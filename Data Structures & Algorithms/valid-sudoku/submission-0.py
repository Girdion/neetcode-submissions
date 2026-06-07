class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[i][j] in seen:
                    return False

                if board[i][j] == '.':
                    continue
                else:
                    seen.add(board[i][j])
        
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[j][i] in seen:
                    return False

                if board[j][i] == '.':
                    continue
                else:
                    seen.add(board[j][i])

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()

                for i in range(3):
                    for j in range(3):
                        val = board[row + i][col + j]

                        if val == '.':
                            continue

                        if val in seen:
                            return False

                        seen.add(val)

        
        return True
        