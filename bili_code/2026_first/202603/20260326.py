"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。
每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

示例 2：
输入： heights = [2,4]
输出： 4

https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
"""


class Solution:
    def largestRectangleArea(self, heights) -> int:
        res = 0
        stack = []
        for i, n in enumerate(heights):
            if not stack:
                stack.append([i, n])
            else:
                while stack and n < stack[-1][-1]:
                    out_s = stack[-1]
                    if len(stack) >= 2:
                        last_min = stack[-2]
                        res = max((i - last_min[0] - 1) * out_s[1], res)
                    else:
                        res = max(i * out_s[1], res)
                    stack.pop()
                stack.append([i, n])
            # print(stack)
        for i, s in enumerate(stack):
            if i > 0:
                res = max((len(heights) - stack[i - 1][0] - 1) * s[1], res)
            else:
                res = max(len(heights) * s[1], res)
        return res

    def largestRectangleArea_1(self, heights) -> int:
        res = 0
        stack = []
        heights = [0] + heights + [0]
        for i, n in enumerate(heights):
            if not stack:
                stack.append([i, n])
            else:
                while stack and n < stack[-1][-1]:
                    out_s = stack[-1]
                    if len(stack) >= 2:
                        last_min = stack[-2]
                        res = max((i - last_min[0] - 1) * out_s[1], res)
                    else:
                        res = max(i * out_s[1], res)
                    stack.pop()
                stack.append([i, n])
            # print(stack)

        return res


if __name__ == '__main__':
    res = Solution().largestRectangleArea_1(heights=[2, 1, 2])
    print(res)
