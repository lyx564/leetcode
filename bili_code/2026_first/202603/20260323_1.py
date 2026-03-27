"""
516. 最长回文子序列
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

示例 1：
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。

示例 2：
输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
https://leetcode.cn/problems/longest-palindromic-subsequence/
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s = list(s)
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    if abs(i-j) == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    if abs(i - j) == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        print('   ' + '  '.join(s))
        for i, x in enumerate(dp):
            print(s[i], x)
        return dp[0][n-1]


if __name__ == '__main__':
    res = Solution().longestPalindromeSubseq(s = "bbbab")
    print(res)
