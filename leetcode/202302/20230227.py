"""
给你一个整数数组nums，每次 操作会从中选择一个元素并 将该元素的值减少1。
如果符合下列情况之一，则数组A就是 锯齿数组：
每个偶数索引对应的元素都大于相邻的元素，即A[0] > A[1] < A[2] > A[3] < A[4] > ...
或者，每个奇数索引对应的元素都大于相邻的元素，即A[0] < A[1] > A[2] < A[3] > A[4] < ...
返回将数组nums转换为锯齿数组所需的最小操作次数。

示例 1：
输入：nums = [1,2,3]
输出：2
解释：我们可以把 2 递减到 0，或把 3 递减到 1。

示例 2：
输入：nums = [9,6,1,6,2]
输出：4

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/decrease-elements-to-make-array-zigzag
"""


class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        res1, res2 = 0, 0
        num_bak = nums.copy()
        n_len = len(nums)
        if n_len < 2:
            return 0
        for i in range(0, n_len, 2):
            if i == 0:
                two_min = nums[1]
            elif i == n_len - 1:
                two_min = nums[n_len - 2]
            else:
                two_min = min(nums[i-1], nums[i+1])
            if two_min <= nums[i]:
                sub = nums[i] - two_min + 1
                res1 += sub
                num_bak[i] -= sub
        print(num_bak, res1)
        num_bak = nums.copy()

        for i in range(1, n_len, 2):
            if i == n_len - 1:
                two_min = nums[n_len - 2]
            else:
                two_min = min(nums[i-1], nums[i+1])
            if two_min <= nums[i]:
                sub = nums[i] - two_min + 1
                res2 += sub
                num_bak[i] -= sub
        print(num_bak, res2)
        return min(res1, res2)


if __name__ == '__main__':
    res = Solution().movesToMakeZigzag(nums=[3,10,7,9,9,3,6,9,4])
    print(res)
