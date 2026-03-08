"""
51. N 皇后
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]

https://leetcode.cn/problems/n-queens/

"""


class Solution:
    def solveNQueens(self, n: int):
        self.res = []

        def if_ok(now_board, i, j):
            for k in range(i):
                if now_board[k][j] == 'Q':
                    return False
            target_i, target_j = i, j
            while 0 <= target_i < n and 0 <= target_j < n:
                if now_board[target_i][target_j] == 'Q':
                    return False
                target_i -= 1
                target_j += 1

            target_i, target_j = i, j
            while 0 <= target_i < n and 0 <= target_j < n:
                if now_board[target_i][target_j] == 'Q':
                    return False
                target_i -= 1
                target_j -= 1

            return True

        def backtrace(now_i, now_res):
            if now_i == n:
                new_res = [''.join(x) for x in now_res.copy()]
                self.res.append(new_res)
                return

            for j in range(n):
                if if_ok(now_res, now_i, j):
                    now_res[now_i][j] = 'Q'
                    backtrace(now_i+1, now_res.copy())
                    now_res[now_i][j] = '.'

        backtrace(0, [['.' for _ in range(n)] for _ in range(n)])
        return self.res



if __name__ == '__main__':
    res = Solution().solveNQueens(n=4)
    print(res)
