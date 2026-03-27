"""
349. 两个数组的交集
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。
我们可以 不考虑输出结果的顺序 。



示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的

https://leetcode.cn/problems/intersection-of-two-arrays/
"""

class Solution:
    def intersection(self, nums1, nums2):
        res_set = set()
        now_set = set()
        for x in nums1:
            now_set.add(x)
        for x in nums2:
            if x in now_set:
                res_set.add(x)
        return list(res_set)





if __name__ == '__main__':
    res = Solution().intersection(nums1=[1, 2, 2, 1], nums2=[2, 2])
    print(res)