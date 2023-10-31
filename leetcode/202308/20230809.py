"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

示例 2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/nge-tou-zi-de-dian-shu-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def dicesProbability(self, n: int):
        dp = [1/6] * 6
        for i in range(2, n+1):
            new = [0]*(5*i+1)
            for j in range(6):
                for k in range(len(dp)):
                    new[j+k] += dp[k] / 6
            dp = new
        return dp


if __name__ == '__main__':
    res = Solution().dicesProbability(n = 2)
    print(res)
