"""
392. 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：
如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true

示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false

https://leetcode.cn/problems/is-subsequence/

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]  # s[:i+1]是否为t[:j+1]的子序列
        for j in range(n+1):
            dp[0][j] = True
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        for p in dp:
            print(p)
        return dp[-1][-1]


if __name__ == '__main__':
    res = Solution().isSubsequence(s = "abc", t = "ahbgdc")
    print(res)