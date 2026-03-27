"""
583. 两个字符串的删除操作

给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
每步 可以删除任意一个字符串中的一个字符。

示例 1：
输入: word1 = "sea", word2 = "eat"
输出: 2
解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"

示例  2:
输入：word1 = "leetcode", word2 = "etco"
输出：4
https://leetcode.cn/problems/delete-operation-for-two-strings/description/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1, word2 = list(word1), list(word2)
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0] = i
        for j in range(n2+1):
            dp[0][j] = j

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)

        print('      ' + '  '.join(list(word2)))
        for i, d in enumerate(dp):
            if i == 0:
                print(' ', d)
            else:
                print(word1[i-1], d)
        return dp[-1][-1]


if __name__ == '__main__':
    res = Solution().minDistance(word1 = "sea", word2 = "eat")
    print(res)