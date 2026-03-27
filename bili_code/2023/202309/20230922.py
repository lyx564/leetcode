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

提示：
1 <= n <= 20

https://leetcode.cn/problems/combinations/

"""

class Solution:
    def combine(self, n: int, k: int):
        if n == k:
            return [[x+1 for x in range(n)]]
        if k == 0:
            return []
        if k == 1:
            return [[x+1] for x in range(n)]

        res = []

        def digui(now_n, now_res):
            if len(now_res) == k:
                res.append(now_res)
                return

            for i in range(now_n, n-(k - len(now_res))+1):
                digui(i+1, now_res + [i+1])

        digui(0, [])
        return res

    def combine_2(self, n: int, k: int):
        if n == k:
            return [[x+1 for x in range(n)]]
        if k == 0:
            return []
        if k == 1:
            return [[x+1] for x in range(n)]
        res1 = self.combine_2(n-1, k-1)
        res = []
        for i in res1:
            for j in range(i[-1]+1, n+1):
                res.append(i + [j])
        return res


if __name__ == '__main__':
    res = Solution().combine(n=4, k=3)
    print(res)

    # 4   3
    # 1, 2, 3
    # 1, 3, 4
    # 1, 2, 4
    # 2, 3, 4
    #
    # 3  2
    #
    # 1, 2
    # 1, 3
    # 2, 3