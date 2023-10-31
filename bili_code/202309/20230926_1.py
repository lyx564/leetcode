"""
491. 递增子序列
给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。

示例 1：
输入：nums = [4,6,7,7]
输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

示例 2：
输入：nums = [4,4,3,2,1]
输出：[[4,4]]

https://leetcode.cn/problems/non-decreasing-subsequences/

"""

class Solution:
    def findSubsequences(self, nums):
        self.res = []

        def digui(now_idx, now_res):
            if now_idx > len(nums):
                return
            if len(now_res) > 1:
                self.res.append(now_res)
            history = set()
            for i in range(now_idx, len(nums)):
                if nums[i] in history:
                    continue
                history.add(nums[i])
                if not now_res or now_res[-1] <= nums[i]:
                    digui(i+1, now_res+[nums[i]])
        digui(0, [])
        return self.res


if __name__ == '__main__':
    res = Solution().findSubsequences(nums=[4,4,3,2,1])
    print(res)