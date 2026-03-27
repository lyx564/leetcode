"""
115. 不同的子序列
给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 109 + 7 取模。

示例 1：
输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。


示例 2：
输入：s = "babgbag", t = "bag"
输出：5
解释：
如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。
https://leetcode.cn/problems/distinct-subsequences/

"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s, t = list(s), list(t)
        n_s, n_t = len(s), len(t)
        dp = [[0 for _ in range(n_s+1)] for _ in range(n_t+1)]
        for j in range(n_s+1):
            dp[0][j] = 1
        for i in range(1, n_t+1):
            for j in range(i, n_s+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        # print('      ' + '  '.join(list(s)))
        # for i, d in enumerate(dp):
        #     if i == 0:
        #         print(' ', d)
        #     else:
        #         print(t[i-1], d)
        return dp[-1][-1]


if __name__ == '__main__':
    res = Solution().numDistinct(s = "rabbbit", t = "rabbit")
    print(res)
