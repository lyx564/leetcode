
"""
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100

https://leetcode.cn/problems/partition-equal-subset-sum/
"""


class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n)]
        for j in range(target+1):
            if nums[0] == j:
                dp[0][j] = True
        for i in range(1, n):
            for j in range(1, target+1):
                if j == nums[i]:
                    dp[i][j] = True
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        print(dp)
        return dp[n-1][target]

    def canPartition_1(self, nums) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        n = len(nums)
        dp = [False for _ in range(target+1)]
        for j in range(target+1):
            if nums[0] == j:
                dp[j] = True
        for i in range(1, n):
            for j in range(target, 0, -1):
                if j == nums[i]:
                    dp[j] = True
                elif j > nums[i]:
                    dp[j] = dp[j] or dp[j-nums[i]]
        print(dp)
        return dp[target]


if __name__ == '__main__':
    res = Solution().canPartition_1(nums=[1, 5, 11, 5])
    print(res)
