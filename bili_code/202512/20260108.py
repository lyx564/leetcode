"""
977. 有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums 已按 非递减顺序 排序

进阶：
请你设计时间复杂度为 O(n) 的算法解决本问题

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/squares-of-a-sorted-array/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def sortedSquares(self, nums):
        res = []
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        l, r = i - 1, i
        while l >= 0 and r < len(nums):
            if nums[l] ** 2 <= nums[r] ** 2:
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[r] ** 2)
                r += 1
        while l >= 0:
            res.append(nums[l] ** 2)
            l -= 1
        while r < len(nums):
            res.append(nums[r] ** 2)
            r += 1
        return res

    def sortedSquares_1(self, nums):
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        idx = len(nums) - 1
        while l <= r:
            if nums[l] ** 2 <= nums[r] ** 2:
                res[idx] = nums[r] ** 2
                r -= 1
            else:
                res[idx] = nums[l] ** 2
                l += 1
            idx -= 1

        return res


if __name__ == '__main__':
    res = Solution().sortedSquares_1([-4, -1, 0, 3, 10])
    print(res)
