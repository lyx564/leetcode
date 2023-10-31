"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        history = [[0 for _ in range(n)] for _ in range(m)]

        def digui(i, j, w):
            if w == '':
                return True
            if i >= m or i < 0 or j < 0 or j >= n:
                return False
            if i < m and j < n and history[i][j] == 0 and board[i][j] == w[0]:
                if len(w) == 1:
                    return True
                history[i][j] = 1
                exist = digui(i+1, j, w[1:]) or digui(i, j+1, w[1:]) or digui(i-1, j, w[1:]) or digui(i, j-1, w[1:])
                history[i][j] = 0
                return exist

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = digui(i, j, word)
                    if res:
                        return True
        return False


if __name__ == '__main__':
    res = Solution().exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCEF")
    print(res)