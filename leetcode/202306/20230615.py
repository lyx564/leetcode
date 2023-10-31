"""
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例1:
输入: [1,2,3,4,5]
输出: True

示例2:
输入: [0,0,1,2,5]
输出: True

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def isStraight(self, nums) -> bool:
        nums_set = set(nums)
        zero_num = 0
        start = 14
        for n in nums:
            if n == 0:
                zero_num += 1
            else:
                start = min(start, n)

        no_zero_num = len(nums) - zero_num
        while no_zero_num > 0:
            if start in nums_set:
                no_zero_num -= 1
            elif zero_num > 0:
                zero_num -= 1
            else:
                return False
            start += 1
        return True


    def isStraight_2(self, nums) -> bool:
        nums.sort()
        zero_num = 0
        while nums[zero_num] == 0:
            zero_num += 1
        now_num = nums[zero_num]
        i = zero_num + 1
        while i < len(nums):
            if nums[i] != now_num + 1 and zero_num == 0:
                return False
            if nums[i] == now_num + 1:
                i += 1
            else:
                zero_num -= 1
            now_num += 1
        return True






if __name__ == '__main__':
    res = Solution().isStraight_2(nums=[0,2,7,3,5])
    print(res)