"""
45. 跳跃游戏 II
给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。
每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：
0 <= j <= nums[i] 且
i + j < n
返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。

示例 1:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:
输入: nums = [2,3,0,1,4]
输出: 2

https://leetcode.cn/problems/jump-game-ii/
"""


class Solution:
    def jump(self, nums) -> int:
        max_pos = 0
        step = 0
        end = 0
        for i in range(len(nums) - 1):
            if i <= max_pos:
                max_pos = max(max_pos, i + nums[i])
            if i == end:
                step += 1
                end = max_pos
        return step

    def jump_1(self, nums) -> int:
        dp = [len(nums) for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)-1):
            for j in range(i+1, min(len(nums), i+nums[i]+1)):
                dp[j] = min(dp[j], dp[i]+1)

        return dp[-1]



if __name__ == '__main__':
    res = Solution().jump_1(nums=[2,1])
    print(res)
