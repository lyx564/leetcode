"""
77. 组合
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2：
输入：n = 1, k = 1
输出：[[1]]

https://leetcode.cn/problems/combinations/description/
"""


class Solution:
    def combine(self, n: int, k: int):
        self.res = []
        def backtrace(now_n, now_k, now_res):
            if now_k == 0:
                self.res.append(now_res)
                return
            for i in range(now_n, n+1):
                backtrace(i+1, now_k-1, now_res+[i])
        backtrace(1, k, [])
        return self.res




if __name__ == '__main__':
    res = Solution().combine(n = 4, k = 3)
    print(res)
