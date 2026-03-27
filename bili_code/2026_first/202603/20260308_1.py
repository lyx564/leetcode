"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

https://leetcode.cn/problems/subsets/
"""


class Solution:
    def subsets(self, nums):
        self.res = []

        def backtrace(now_idx, now_res):
            if len(now_res) > len(nums):
                return
            if now_idx > len(nums):
                return
            self.res.append(now_res)
            for i in range(now_idx, len(nums)):
                now_num = nums[i:i+1]
                backtrace(i+1, now_res + now_num)
        backtrace(0, [])
        return self.res

    def subsets_1(self, nums):
        res = [[]]
        for n in nums:
            now_res = res.copy()
            for r in now_res:
                now_r = r + [n]
                res.append(now_r)
        return res


if __name__ == '__main__':
    res = Solution().subsets_1(nums=[1,2,3])
    print(res)