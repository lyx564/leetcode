"""
90. 子集 II
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

https://leetcode.cn/problems/subsets-ii/

"""

class Solution:
    def subsetsWithDup(self, nums):
        self.res = [[]]
        nums.sort()

        def digui(now_idx, now_res):
            if now_idx >= len(nums):
                return
            for i in range(now_idx, len(nums)):
                if i > now_idx and nums[i] == nums[i-1]:
                    continue
                self.res.append(now_res+[nums[i]])
                digui(i+1, now_res+[nums[i]])

        digui(0, [])
        return self.res


if __name__ == '__main__':
    res = Solution().subsetsWithDup(nums = [1,2,2])
    print(res)