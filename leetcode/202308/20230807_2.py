"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/chou-shu-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [9999999 for _ in range(n)]
        res[0] = 1
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            num2, num3, num5 = res[p2] * 2, res[p3] * 3, res[p5] * 5
            res[i] = min(num2, num3, num5)
            if res[i] == num2:
                p2 += 1
            if res[i] == num3:
                p3 += 1
            if res[i] == num5:
                p5 += 1
        return res[-1]


if __name__ == '__main__':
    res = Solution().nthUglyNumber(n=10)
    print(res)