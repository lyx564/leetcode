"""
实现pow(x,n)，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        reverse = False
        if n < 0:
            reverse = True
            n = -n
        res = x
        add = []
        while n > 1:
            if n % 2 == 1:
                add.append(res)
            res = res * res
            n //= 2
        print(add)
        if add:
            for a in add:
                res *= a
        if reverse:
            res = 1/res
        return res

    def myPow_2(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        reverse = False
        if n < 0:
            reverse = True
            n = -n
        res = 1
        con = x
        while n > 0:
            if n % 2 == 1:
                res *= con
            con = con * con
            n //= 2
        if reverse:
            res = 1/res
        return res


if __name__ == '__main__':
    res = Solution().myPow_2(x=2, n=21)
    print(res)