"""
131. 分割回文串
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成

https://leetcode.cn/problems/palindrome-partitioning/

"""

class Solution:
    def partition(self, s: str):
        n = len(s)
        self.res = []

        def digui(now_idx, now_res):
            if now_idx == n:
                self.res.append(now_res)
                return

            for i in range(now_idx, n):
                now_s = s[now_idx:i+1]
                if now_s == now_s[::-1]:
                    digui(i+1, now_res + [now_s])
        digui(0, [])
        return self.res





if __name__ == '__main__':
    res = Solution().partition(s = "abbab")
    print(res)
