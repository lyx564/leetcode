"""
我们从一块字母板上的位置(0, 0)出发，该坐标对应的字符为board[0][0]。
在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。

我们可以按下面的指令规则行动：
如果方格存在，'U'意味着将我们的位置上移一行；
如果方格存在，'D'意味着将我们的位置下移一行；
如果方格存在，'L'意味着将我们的位置左移一列；
如果方格存在，'R'意味着将我们的位置右移一列；
'!'会把在我们当前位置 (r, c) 的字符board[r][c]添加到答案中。
（注意，字母板上只存在有字母的位置。）

返回指令序列，用最小的行动次数让答案和目标target相同。你可以返回任何达成目标的路径。

示例 1：
输入：target = "leet"
输出："DDR!UURRR!!DDD!"

示例 2：
输入：target = "code"
输出："RR!DDRR!UUL!R!"

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/alphabet-board-path
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = ''
        pos = [0, 0]
        for w in target:
            des = [(ord(w) - ord('a')) // 5, (ord(w) - ord('a')) % 5]
            if pos != des:
                if pos == [5, 0]:
                    pos[0] -= 1
                    res = res + 'U'
                if pos[1] < des[1]:
                    res = res + 'R' * (des[1] - pos[1])
                else:
                    res = res + 'L' * (pos[1] - des[1])
                if pos[0] < des[0]:
                    res = res + 'D' * (des[0] - pos[0])
                else:
                    res = res + 'U' * (pos[0] - des[0])
                pos = des
            res = res + '!'
        return res


if __name__ == '__main__':
    res = Solution().alphabetBoardPath(target = "zz")
    print(res)