"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
示例 1:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxValue(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        left, top = grid[0][0], [0 for _ in range(n)]
        top[0] = grid[0][0]
        for j in range(1, n):
            top[j] = top[j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    left = 0
                res = max(left, top[j]) + grid[i][j]
                left = res
                top[j] = res

        return top[n-1]


if __name__ == '__main__':
    res = Solution().maxValue(grid=[
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ])
    print(res)
