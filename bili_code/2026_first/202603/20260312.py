"""
343. 整数拆分
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
返回 你可以获得的最大乘积 。

示例 1:
输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

提示:
2 <= n <= 58

https://leetcode.cn/problems/integer-break/
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        for i in range(3, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], max(j, dp[j])*max(i-j, dp[i-j]))
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    res = Solution().integerBreak(n=10)
    print(res)