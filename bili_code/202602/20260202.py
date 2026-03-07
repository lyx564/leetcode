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
        all_res = []
        nums = sorted(nums)
        for i in range(len(nums)-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                now_sum = nums[i] + nums[j]
                if now_sum > target > 0:
                    break
                l, r = j+1, len(nums)-1
                while l < r:
                    if now_sum + nums[l] + nums[r] > target:
                        r -= 1
                        while l < r and nums[r+1] == nums[r]:
                            r -= 1
                    elif now_sum + nums[l] + nums[r] < target:
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                    else:
                        all_res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                        while l < r and nums[r+1] == nums[r]:
                            r -= 1

        return all_res



if __name__ == '__main__':
    res = Solution().fourSum(nums=[-9,-2,7,6,-8,5,8,3,-10,-7,8,-8,0,0,1,-8,7], target=4)
    print(res)