class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        centers = [(1, 1), (1, 4), (1,7), (4, 1), (4, 4), 
        (4,7), (7, 1), (7,4), (7,7)]


        i, j = 0, 0

        while(i < 9):
            row_dict = set()
            column_dict = set()
            for k in range(9):
                if board[i][k] in row_dict and board[i][k] != '.':
                    return False
                if board[k][j] in column_dict and board[k][j] != '.':
                    return False
                row_dict.add(board[i][k])
                column_dict.add(board[k][j])

            i+=1
            j+=1
        
        for (i, j) in centers:
            box_dict = set()
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if board[k][l] == '.':
                        continue
                    if board[k][l] in box_dict:
                        return False
                    box_dict.add(board[k][l])
                    
        return True