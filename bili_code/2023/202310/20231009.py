"""
474. 一和零
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

示例 1：
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

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
        n_strs = len(strs)
        nums_0_1 = []
        for s in strs:
            num0, num1 = 0, 0
            for c in s:
                if c == '1':
                    num1 += 1
                else:
                    num0 += 1
            nums_0_1.append([num0, num1])
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(n_strs)]
        for i in range(m+1):
            for j in range(n+1):
                if nums_0_1[0][0] <= i and nums_0_1[0][1] <= j:
                    dp[0][i][j] = 1
        for i in range(1, n_strs):
            for j in range(m+1):
                for k in range(n+1):
                    now_num0, now_num1 = nums_0_1[i][0], nums_0_1[i][1]
                    if j >= now_num0 and k >= now_num1:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-now_num0][k-now_num1]+1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        return dp[n_strs-1][m][n]

    def findMaxForm_1(self, strs, m: int, n: int) -> int:
        n_strs = len(strs)
        nums_0_1 = []
        for s in strs:
            num0, num1 = 0, 0
            for c in s:
                if c == '1':
                    num1 += 1
                else:
                    num0 += 1
            nums_0_1.append([num0, num1])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if nums_0_1[0][0] <= i and nums_0_1[0][1] <= j:
                    dp[i][j] = 1
        for i in range(1, n_strs):
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    now_num0, now_num1 = nums_0_1[i][0], nums_0_1[i][1]
                    if j >= now_num0 and k >= now_num1:
                        dp[j][k] = max(dp[j][k], dp[j-now_num0][k-now_num1]+1)

        return dp[m][n]

if __name__ == '__main__':
    res = Solution().findMaxForm_1(strs=["10", "0001", "111001", "1", "0"], m=5, n=3)
    print(res)
