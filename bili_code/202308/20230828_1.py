"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]

提示：
1 <= n <= 20

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/spiral-matrix-ii/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def generateMatrix(self, n: int):
        res = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        i, j = 0, 0
        top, down, left, right = 0, n-1, 0, n-1
        now_dir = [0, 1]
        while num <= n*n:
            res[i][j] = num
            num += 1
            i, j = i + now_dir[0], j + now_dir[1]
            if now_dir == [0, 1] and j == right:
                now_dir = [1, 0]
                top += 1
            elif now_dir == [1, 0] and i == down:
                now_dir = [0, -1]
                right -= 1
            elif now_dir == [0, -1] and j == left:
                now_dir = [-1, 0]
                down -= 1
            elif now_dir == [-1, 0] and i == top:
                now_dir = [0, 1]
                left += 1
        return res


if __name__ == '__main__':
    res = Solution().generateMatrix(n=3)
    print(res)