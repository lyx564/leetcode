"""
统计一个数字在排序数组中出现的次数。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def search(self, nums, target: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] <= target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
        right = i
        print(right)
        i = 0
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] >= target:
                j = mid - 1
        left = j
        print(left)
        res = right - left - 1
        print(res)
        return res


if __name__ == '__main__':
    res = Solution().search(nums=[5,7,7,8,8,10], target=8)
    print(res)
