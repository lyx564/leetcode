"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def maxSubArray(self, nums) -> int:
        res = nums[0]
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            res = max(res, dp[i])
        print(dp)
        return res

if __name__ == '__main__':
    res = Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])
    print(res)