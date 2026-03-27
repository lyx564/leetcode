"""
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

https://leetcode.cn/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums, target: int):
        sorted_nums = sorted(nums, reverse=False)
        l, r = 0, len(sorted_nums) - 1
        while l < r and sorted_nums[l] + sorted_nums[r] != target:
            if sorted_nums[l] + sorted_nums[r] < target:
                l += 1
            else:
                r -= 1
        target_l_v, target_r_v = sorted_nums[l], sorted_nums[r]
        res_l, res_r = -1, -1
        for i in range(len(nums)):
            if res_l == -1 and nums[i] == target_l_v:
                res_l = i
            elif res_r == -1 and nums[i] == target_r_v:
                res_r = i

        return [res_l, res_r]

    def twoSum_1(self, nums, target: int):
        value_2_idx = {}
        for i in range(len(nums)):
            if target - nums[i] not in value_2_idx:
                value_2_idx[nums[i]] = i
            else:
                return [value_2_idx[target - nums[i]], i]


if __name__ == '__main__':
    res = Solution().twoSum(nums=[2,5,5,11], target=10)
    print(res)