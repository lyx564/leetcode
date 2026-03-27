"""
474. 一和零
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

示例 1：
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。
{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

示例 2：
输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。

提示：
1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100

https://leetcode.cn/problems/ones-and-zeroes/
"""


class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        idx_2_count = {}
        s_n = len(strs)
        for i, s in enumerate(strs):
            idx_2_count[i] = {0: 0, 1: 0}
            for x in list(s):
                idx_2_count[i][int(x)] += 1
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(s_n)]
        zero_count, one_count = idx_2_count[0][0], idx_2_count[0][1]
        for j in range(m+1):
            for k in range(n+1):
                if zero_count <= j and one_count <= k:
                    dp[0][j][k] = 1

        for i in range(1, s_n):
            for j in range(m + 1):
                for k in range(n + 1):
                    zero_count, one_count = idx_2_count[i][0], idx_2_count[i][1]
                    if j >= zero_count and k >= one_count:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zero_count][k-one_count]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        return dp[-1][-1][-1]


    def findMaxForm_1(self, strs, m: int, n: int) -> int:
        idx_2_count = {}
        s_n = len(strs)
        for i, s in enumerate(strs):
            idx_2_count[i] = {0: 0, 1: 0}
            for x in list(s):
                idx_2_count[i][int(x)] += 1
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        zero_count, one_count = idx_2_count[0][0], idx_2_count[0][1]
        for j in range(m+1):
            for k in range(n+1):
                if zero_count <= j and one_count <= k:
                    dp[j][k] = 1

        for i in range(1, s_n):
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    zero_count, one_count = idx_2_count[i][0], idx_2_count[i][1]
                    if j >= zero_count and k >= one_count:
                        dp[j][k] = max(dp[j][k], dp[j-zero_count][k-one_count]+1)
        return dp[-1][-1]
    


if __name__ == '__main__':
    res = Solution().findMaxForm_1(strs = ["101000000","1100001010","11101000","011010110","0010001","0011","0111101111"], m = 10, n = 11)
    print(res)
