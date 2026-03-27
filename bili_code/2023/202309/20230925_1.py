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

提示：
1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

https://leetcode.cn/problems/subsets/
"""


class Solution:
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            new_r = [num + [n] for num in res]
            res = res + new_r
        return res


    def subsets_2(self, nums):
        self.res = [[]]

        def digui(now_idx, now_res):
            if now_idx >= len(nums):
                return
            for i in range(now_idx, len(nums)):
                self.res.append(now_res + [nums[i]])
                digui(i+1, now_res + [nums[i]])

        digui(0, [])
        return self.res


if __name__ == '__main__':
    res = Solution().subsets_2(nums=[1, 2, 3])
    print(res)
