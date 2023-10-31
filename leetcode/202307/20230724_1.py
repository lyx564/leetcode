"""
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
输入: n = 5, m = 3
输出: 3

示例 2：
输入: n = 10, m = 17
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = [i for i in range(n)]
        idx = 0
        while len(nums) > 1:
            idx = (idx + m - 1) % len(nums)
            nums.pop(idx)

        return nums[0]

    # def lastRemaining_1(self, n: int, m: int) -> int:
    #     import sys
    #     sys.setrecursionlimit(100000)
    #     nums = [i for i in range(n)]
    #
    #     def digui(nums, m, idx):
    #         if len(nums) == 1:
    #             return nums[0]
    #         idx = (idx + m - 1) % len(nums)
    #         nums.pop(idx)
    #         return digui(nums, m, idx)
    #     return digui(nums, m, 0)


if __name__ == '__main__':
    res = Solution().lastRemaining(n=5, m=3)
    print(res)