"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：
输入：matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        top, down, left, right = 0, m-1, 0, n-1
        x, y = 0, 0
        res = [matrix[x][y]]
        while len(res) < m*n:
            while y < right and len(res) < m*n:
                y += 1
                res.append(matrix[x][y])
            top += 1
            while x < down and len(res) < m*n:
                x += 1
                res.append(matrix[x][y])
            right -= 1
            while y > left and len(res) < m*n:
                y -= 1
                res.append(matrix[x][y])
            down -= 1
            while x > top and len(res) < m*n:
                x -= 1
                res.append(matrix[x][y])
            left += 1
        return res


if __name__ == '__main__':
    res = Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    print(res)