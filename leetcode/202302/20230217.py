"""
给你一个由若干 0 和 1 组成的二维网格grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。
示例 1：
输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9

示例 2：
输入：grid = [[1,1,0,0]]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/largest-1-bordered-square
"""


class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        left = [[0 for _ in range(n)] for _ in range(m)]
        up = [[0 for _ in range(n)] for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 and j == 0:
                        left[0][0] = 1
                        up[0][0] = 1
                    if i == 0 and j > 0:
                        up[0][j] = 1
                        left[0][j] = left[0][j - 1] + 1
                    if j == 0 and i > 0:
                        left[i][0] = 1
                        up[i][0] = up[i - 1][0] + 1
                    if i > 0 and j > 0:
                        left[i][j] = left[i][j-1] + 1
                        up[i][j] = up[i-1][j] + 1
                    border = min(left[i][j], up[i][j])
                    while left[i-border+1][j] < border or up[i][j-border+1] < border:
                        border -= 1
                    res = max(res, border)
        return res ** 2

if __name__ == '__main__':
    res = Solution().largest1BorderedSquare(grid = [[1,1,1],[1,0,1],[1,1,1]])
    print(res)