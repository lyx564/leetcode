"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 借助集合，空间复杂度O(n)
    def findRepeatNumber(self, nums) -> int:
        history = set()
        for n in nums:
            if n in history:
                return n
            else:
                history.add(n)
        return None

    # 原地旋转，空间复杂度O(1)
    def findRepeatNumber_v2(self, nums) -> int:
        i = 0
        while i < len(nums):
            while nums[i] != nums[nums[i]]:
                temp1 = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp1
            if i == nums[i]:
                i += 1
            else:
                return nums[i]
        return None



if __name__ == '__main__':
    res = Solution().findRepeatNumber_v2(nums=[3, 1, 2, 3, 4, 5, 4])
    print(res)