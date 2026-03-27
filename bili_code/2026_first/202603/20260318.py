"""
718. 最长重复子数组
给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。
示例 1：
输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。

示例 2：
输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5

https://leetcode.cn/problems/maximum-length-of-repeated-subarray/

"""

class Solution:
    def findLength(self, nums1, nums2) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        res = 0
        dp = [[0 for _ in range(n2)] for _ in range(n1)]
        if nums1[0] == nums2[0]:
            dp[0][0] = 1
            res = 1
        for i in range(1, n1):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
                res = 1
        for j in range(1, n2):
            if nums1[0] == nums2[j]:
                dp[0][j] = 1
                res = 1
        for i in range(1, n1):
            for j in range(1, n2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                    res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    res = Solution().findLength(nums1 =[0,1,1,1,1], nums2 = [1,0,1,0,1])
    print(res)