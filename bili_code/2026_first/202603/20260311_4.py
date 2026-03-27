"""
738. 单调递增的数字
当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

示例 1:
输入: n = 10
输出: 9

示例 2:
输入: n = 1234
输出: 1234

示例 3:
输入: n = 332
输出: 299

https://leetcode.cn/problems/monotone-increasing-digits/description/
"""


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        i = 0
        n_str = str(n)
        if len(n_str) == 1:
            return n
        while i < len(n_str)-1 and int(n_str[i]) <= int(n_str[i+1]):
            i += 1
        if i == len(n_str)-1:
            return n

        while i > 0 and n_str[i] == n_str[i-1]:
            i -= 1
        if i == 0:
            return int(str(int(n_str[0])-1) + '9'*(len(n_str)-1))

        return int(n_str[:i] + str(int(n_str[i])-1) + '9'*(len(n_str[i+1:])))

    def monotoneIncreasingDigits_1(self, n: int) -> int:
        n_str = list(str(n))
        i = len(n_str)-1
        while i > 0:
            if n_str[i] < n_str[i-1]:
                j = i
                while j < len(n_str):
                    n_str[j] = '9'
                    j += 1
                n_str[i-1] = str(int(n_str[i-1])-1)
            i -= 1
        return int(''.join(n_str))


if __name__ == '__main__':
    res = Solution().monotoneIncreasingDigits_1(n = 1332)
    print(res)
