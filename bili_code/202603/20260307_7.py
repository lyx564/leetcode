"""
40. 组合总和 II
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]

https://leetcode.cn/problems/combination-sum-ii/
"""


class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        self.res = []

        def backtrace(now_idx, now_target, now_res):
            if now_target == 0:
                self.res.append(now_res)
                return
            if now_target < 0:
                return
            for i in range(now_idx, len(candidates)):
                if i > now_idx and candidates[i] == candidates[i-1]:
                    continue
                now_num = candidates[i]
                backtrace(i+1, now_target-now_num, now_res+[now_num])
        backtrace(0, target, [])
        return self.res


if __name__ == '__main__':
    res = Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
    print(res)
