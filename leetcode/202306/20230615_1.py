"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def numWays(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        return (self.numWays(n-1) + self.numWays(n-2)) % 1000000007



    def numWays_1(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        x, y = 1, 2
        for i in range(3, n+1):
            x, y = y, x + y
        return y % 1000000007




if __name__ == '__main__':
    res = Solution().numWays_1(n=39)
    print(res)