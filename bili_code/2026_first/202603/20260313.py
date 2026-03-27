"""
494. 目标和
给你一个非负整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1

https://leetcode.cn/problems/target-sum/
"""


class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        if sum(nums) < target or -sum(nums) > target:
            return 0
        if (sum(nums) + target) % 2 != 0:
            return 0
        n = len(nums)
        new_target = (sum(nums) + target) // 2

        dp = [[0 for _ in range(new_target + 1)] for _ in range(n)]
        dp[0][0] = 1
        for j in range(new_target + 1):
            if nums[0] == j:
                dp[0][j] += 1

        for i in range(1, n):
            for j in range(new_target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[-1][-1]

    def findTargetSumWays_1(self, nums, target: int) -> int:
        if sum(nums) < target or -sum(nums) > target:
            return 0
        if (sum(nums) + target) % 2 != 0:
            return 0
        n = len(nums)
        new_target = (sum(nums) + target) // 2

        dp = [0 for _ in range(new_target + 1)]
        dp[0] = 1
        for j in range(new_target + 1):
            if nums[0] == j:
                dp[j] += 1

        for i in range(1, n):
            for j in range(new_target, -1, - 1):
                if j >= nums[i]:
                    dp[j] = dp[j] + dp[j - nums[i]]
        # print(dp)
        return dp[-1]

    def findTargetSumWays_2(self, nums, target: int) -> int:
        self.res = 0

        def backtracking(now_idx, now_target):
            if now_target == target and now_idx == len(nums):
                self.res += 1
                return
            if now_idx >= len(nums):
                return
            backtracking(now_idx + 1, now_target + nums[now_idx])
            backtracking(now_idx + 1, now_target - nums[now_idx])

        backtracking(0, 0)
        return self.res


if __name__ == '__main__':
    res = Solution().findTargetSumWays_2(nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], target=0)
    print(res)
