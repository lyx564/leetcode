"""
647. 回文子串
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
回文字符串 是正着读和倒过来读一样的字符串。
子字符串 是字符串中的由连续字符组成的一个序列。

示例 1：
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

https://leetcode.cn/problems/palindromic-substrings/description/
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        s = list(s)
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(1, n):
            if s[i-1] == s[i]:
                dp[i-1][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    if abs(i-j) == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]

        for x in dp:
            print(x)

        return sum(sum(x) for x in dp)


if __name__ == '__main__':
    res = Solution().countSubstrings(s="aaa")
    print(res)
