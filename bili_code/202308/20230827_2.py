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
    def sortedSquares_1(self, nums):
        i = 0
        n_len = len(nums)
        if nums[0] >= 0:
            i = 0
        else:
            while i < n_len - 1 and nums[i] < 0:
                i += 1
            if -nums[i-1] < nums[i]:
                i -= 1

        res = [nums[i]*nums[i]] + [0]*(n_len-1)
        l, r, idx = i-1, i+1, 1
        while idx < n_len:
            if l >= 0 and r < n_len:
                if -nums[l] > nums[r]:
                    small_num = nums[r]
                    r += 1
                else:
                    small_num = nums[l]
                    l -= 1
            elif l >= 0:
                small_num = nums[l]
                l -= 1
            elif r < n_len:
                small_num = nums[r]
                r += 1
            res[idx] = small_num * small_num
            idx += 1
        return res

    def sortedSquares_2(self, nums):
        n_len = len(nums)
        i, j = 0, n_len - 1
        res = [0] * n_len
        idx = n_len - 1
        while i < j:
            while i < j and nums[i] * nums[i] <= nums[j] * nums[j]:
                res[idx] = nums[j] * nums[j]
                idx -= 1
                j -= 1
            while i < j and nums[i] * nums[i] > nums[j] * nums[j]:
                res[idx] = nums[i] * nums[i]
                idx -= 1
                i += 1
        res[idx] = nums[i] * nums[i]
        return res


if __name__ == '__main__':
    res = Solution().sortedSquares_2(nums = [0,3,10])
    print(res)
