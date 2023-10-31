"""
18. 四数之和
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

https://leetcode.cn/problems/4sum/

"""

class Solution:
    def fourSum(self, nums, target: int):
        res = []
        nums.sort()  # [-2, -1, 0, 0, 1, 2]
        for i in range(len(nums)-3):
            if nums[i] >= target > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] >= target > 0:
                    break
                l, r = j + 1, len(nums)-1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum > target:
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif sum < target:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        return res


if __name__ == '__main__':
    res = Solution().fourSum(nums = [2,2,2,2,2], target = 8)
    print(res)