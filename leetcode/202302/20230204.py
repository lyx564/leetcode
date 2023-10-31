"""
给你一个长度为 n的整数数组coins，它代表你拥有的n个硬币。第i个硬币的值为coins[i]。如果你从这些硬币中选出一部分硬币，它们的和为x，那么称，你可以构造出x。
请返回从 0开始（包括0），你最多能构造出多少个连续整数。
你可能有多个相同值的硬币。


示例 1：
输入：coins = [1,3]
输出：2
解释：你可以得到以下这些值：
- 0：什么都不取 []
- 1：取 [1]
从 0 开始，你可以构造出 2 个连续整数。

示例 2：
输入：coins = [1,1,1,4]
输出：8
解释：你可以得到以下这些值：
- 0：什么都不取 []
- 1：取 [1]
- 2：取 [1,1]
- 3：取 [1,1,1]
- 4：取 [4]
- 5：取 [4,1]
- 6：取 [4,1,1]
- 7：取 [4,1,1,1]
从 0 开始，你可以构造出 8 个连续整数。
示例 3：

输入：nums = [1,4,10,3,1]
输出：20

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make
"""


class Solution:
    def getMaximumConsecutive(self, coins) -> int:
        coins.sort()

        res = 1
        for coin in coins:
            if res < coin:
                break
            res += coin
        return res


if __name__ == '__main__':
    coins = [1, 4, 10, 3, 1]
    res = Solution().getMaximumConsecutive(coins)
    print(res)
