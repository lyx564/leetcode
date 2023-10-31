"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
示例 1:

输入: [10,2]
输出: "102"
示例2:

输入: [3,30,34,5,9]
输出: "3033459"

提示:

0 < nums.length <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minNumber_maopao(self, nums) -> str:
        nums = [str(x) for x in nums]
        nums.sort()
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(nums)

    def minNumber_quicksort(self, nums) -> str:
        nums = [str(x) for x in nums]

        def quicksort(nums, l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while i < j and nums[i] + nums[j] <= nums[j] + nums[i]:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                while i < j and nums[i] + nums[j] <= nums[j] + nums[i]:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
            quicksort(nums, l, i-1)
            quicksort(nums, j+1, r)

        quicksort(nums, 0, len(nums)-1)
        return ''.join(nums)


if __name__ == '__main__':
    res = Solution().minNumber_quicksort(nums=[5, 54, 52, 67, 68, 5, 52, 17, 93, 53])
    print(res)
