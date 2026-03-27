"""
37. 解数独
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1：
输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
解释：输入的数独如上图所示，唯一有效的解决方案如下所示：

提示：
board.length == 9
board[i].length == 9
board[i][j] 是一位数字或者 '.'
题目数据 保证 输入数独仅有一个解

https://leetcode.cn/problems/sudoku-solver/

"""

import time

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        empty_list = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                empty_list.append([i, j])

        row_set = {}
        col_set = {}
        min_board_set = {}
        for i in range(9):
            row_set[i] = set()
            for x in board[i]:
                row_set[i].add(x)
        for j in range(9):
            col_set[j] = set()
            for i in range(9):
                col_set[j].add(board[i][j])
        for i in range(9):
            for j in range(9):
                now_idx = i//3*3 + j//3
                if now_idx not in min_board_set:
                    min_board_set[now_idx] = set()
                min_board_set[now_idx].add(board[i][j])

        def backtrace(board, now_idx, row_set, col_set, min_board_set):
            if now_idx == len(empty_list):
                return True

            i, j = empty_list[now_idx]
            for num in range(1, 10):
                num = str(num)
                if num not in row_set[i] and num not in col_set[j] and num not in min_board_set[i//3*3 + j//3]:
                    board[i][j] = num
                    row_set[i].add(num)
                    col_set[j].add(num)
                    min_board_set[i//3*3 + j//3].add(num)
                    res = backtrace(board, now_idx+1, row_set, col_set, min_board_set)
                    if res is True:
                        return True
                    board[i][j] = '.'
                    row_set[i].remove(num)
                    col_set[j].remove(num)
                    min_board_set[i//3*3 + j//3].remove(num)
            return False

        backtrace(board, 0, row_set, col_set, min_board_set)

        return board

    def solveSudoku_1(self, board):

        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                row_used[row].add(num)
                col_used[col].add(num)
                box_used[(row // 3) * 3 + col // 3].add(num)
        self.backtracking(0, 0, board, row_used, col_used, box_used)

        return board

    def backtracking(
            self,
            row: int,
            col: int,
            board,
            row_used,
            col_used,
            box_used,
    ) -> bool:
        if row == 9:
            return True

        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)
        if board[row][col] != ".":
            return self.backtracking(
                next_row, next_col, board, row_used, col_used, box_used
            )

        for num in map(str, range(1, 10)):
            if (
                    num not in row_used[row]
                    and num not in col_used[col]
                    and num not in box_used[(row // 3) * 3 + col // 3]
            ):
                board[row][col] = num
                row_used[row].add(num)
                col_used[col].add(num)
                box_used[(row // 3) * 3 + col // 3].add(num)
                if self.backtracking(
                        next_row, next_col, board, row_used, col_used, box_used
                ):
                    return True
                board[row][col] = "."
                row_used[row].remove(num)
                col_used[col].remove(num)
                box_used[(row // 3) * 3 + col // 3].remove(num)
        return False


if __name__ == '__main__':
    time1 = time.time()
    res = Solution().solveSudoku(
        board=[[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]])
    print(res)
    time2 = time.time()
    print(time2-time1)
