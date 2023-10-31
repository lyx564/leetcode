"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def translateNum(self, num: int) -> int:
        res = []
        dict = {str(i): chr(ord('a') + i) for i in range(26)}

        def dfs(num_s, idx, trans):
            if idx >= len(num_s):
                res.append(trans)
                return
            if num_s[idx:idx+1] in dict:
                dfs(num_s, idx+1, trans+dict[num_s[idx:idx+1]])
            if idx+2 <= len(num_s) and num_s[idx:idx+2] in dict:
                dfs(num_s, idx+2, trans+dict[num_s[idx:idx+2]])

        dfs(str(num), 0, '')
        return len(res)

    def translateNum_1(self, num: int) -> int:
        num, n = str(num), len(str(num))
        l, r, res = 1, 1, 1
        for i in range(1, n):
            res = r
            if 10 <= int(num[i-1:i+1]) <= 25:
                res += l
            l = r
            r = res
        return res


if __name__ == '__main__':
    res = Solution().translateNum_1(num=506)
    print(res)