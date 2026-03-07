"""
131. 分割回文串
给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]

https://leetcode.cn/problems/palindrome-partitioning/
"""


class Solution:
    def partition(self, s: str):
        self.res = []
        def backtrace(now_idx, now_res):
            if now_idx == len(s):
                self.res.append(now_res)
                return

            for i in range(now_idx+1, len(s)+1):
                now_s = s[now_idx:i]
                if i == now_idx+1 or now_s == now_s[::-1]:
                    backtrace(i, now_res+[now_s])

        backtrace(0, [])
        return self.res


if __name__ == '__main__':
    res = Solution().partition(s = "aab")
    print(res)