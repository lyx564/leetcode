"""
518. 零钱兑换 II
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
假设每一种面额的硬币有无限个。
题目数据保证结果符合 32 位带符号整数。

示例 1：
输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2：
输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3 。

示例 3：
输入：amount = 10, coins = [10]
输出：1

提示：

1 <= coins.length <= 300
1 <= coins[i] <= 5000
coins 中的所有值 互不相同
0 <= amount <= 5000

https://leetcode.cn/problems/coin-change-ii/
"""


class Solution:
    def change(self, amount: int, coins) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n)]
        dp[0][0] = 1
        for j in range(1, amount+1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        for i in range(1, n):
            for j in range(amount+1):
                if j >= coins[i]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


    def change_1(self, amount: int, coins) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for j in range(1, amount+1):
            if j % coins[0] == 0:
                dp[j] = 1
        for i in range(1, n):
            for j in range(amount+1):
                if j >= coins[i]:
                    dp[j] += dp[j-coins[i]]
        return dp[-1]

    def change_2(self, amount: int, coins) -> int:
        self.res = 0

        def backtracking(now_idx, now_target):
            if now_target == 0:
                self.res += 1
                return

            for i in range(now_idx, len(coins)):
                if coins[i] <= now_target:
                    backtracking(i, now_target-coins[i])

        backtracking(0, amount)
        return self.res


if __name__ == '__main__':
    res = Solution().change_1(amount=5, coins = [1, 2, 5])
    print(res)
