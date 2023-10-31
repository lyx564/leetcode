"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        res = [0] * (len(nums) - k + 1)
        import collections
        dandiao_quene = collections.deque()
        for i in range(len(nums)):
            num = nums[i]
            if dandiao_quene and i >= dandiao_quene[0][1] + k:
                dandiao_quene.popleft()
            while dandiao_quene and num > dandiao_quene[-1][0]:
                dandiao_quene.pop()
            dandiao_quene.append([num, i])

            if i >= k - 1:
                res[i-k+1] = dandiao_quene[0][0]
            print(i, nums, dandiao_quene, res)

        return res


if __name__ == '__main__':
    res = Solution().maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3)
    print(res)
