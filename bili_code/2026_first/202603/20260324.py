"""
739. 每日温度
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
https://leetcode.cn/problems/daily-temperatures/description/
"""


class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):
            if not stack or t <= stack[-1][1]:
                stack.append((i, t))
            else:
                while stack != [] and t > stack[-1][1]:
                    output_s = stack[-1]
                    stack.pop()
                    res[output_s[0]] = i - output_s[0]
                stack.append((i, t))
        return res


if __name__ == '__main__':
    res = Solution().dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73])
    print(res)
