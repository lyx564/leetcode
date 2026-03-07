"""
454. 四数相加 II
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

示例 1：
输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
两个元组如下：
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

示例 2：
输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
输出：1

https://leetcode.cn/problems/4sum-ii/

"""

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        def get_sum_dict(nums1, nums2):
            sum_dict = {}
            for n1 in nums1:
                for n2 in nums2:
                    if n1 + n2 not in sum_dict:
                        sum_dict[n1+n2] = 0
                    sum_dict[n1 + n2] += 1
            return sum_dict

        res = 0
        sum_dict_1 = get_sum_dict(nums1, nums2)
        sum_dict_2 = get_sum_dict(nums3, nums4)
        for k in sum_dict_1.keys():
            if -k in sum_dict_2:
                res += sum_dict_1[k] * sum_dict_2[-k]

        return res

if __name__ == '__main__':
    res = Solution().fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2])
    print(res)