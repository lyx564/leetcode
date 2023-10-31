"""
给你一份工作时间表hours，上面记录着某一位员工每天的工作小时数。
我们认为当员工一天中的工作小时数大于8小时的时候，那么这一天就是「劳累的一天」。
所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
请你返回「表现良好时间段」的最大长度。

示例 1：
输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。

示例 2：
输入：hours = [6,6,6]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-well-performing-interval
"""


class Solution:
    def longestWPI(self, hours) -> int:
        res, s = 0, 0
        pos = {}
        for i in range(len(hours)):
            s += 1 if hours[i] > 8 else -1
            if s > 0:
                res = max(res, i + 1)
            elif s - 1 in pos:
                res = max(res, i - pos[s - 1])
            if s not in pos:
                pos[s] = i
        return res


if __name__ == '__main__':
    res = Solution().longestWPI(hours=[6, 9, 9, 6, 0, 6, 6, 9])
    print(res)
