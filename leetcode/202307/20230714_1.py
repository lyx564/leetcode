"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

输入: [7,5,6,4]
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def reversePairs(self, nums) -> int:
        def merge_sort(l, r):
            # 终止条件
            if l >= r: return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r+1] = nums[l:r+1]
            for idx in range(l, r+1):
                if i < m+1 and j < r+1 and tmp[i] > tmp[j]:
                    nums[idx] = tmp[j]
                    j += 1
                    res += m-i+1
                elif j == r+1 or i < m+1 and tmp[i] <= tmp[j]:
                    nums[idx] = tmp[i]
                    i += 1
                elif i == m+1:
                    nums[idx] = tmp[j]
                    j += 1

                # print(nums, tmp)

            return res

        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)


if __name__ == '__main__':
    res = Solution().reversePairs(nums=[7, 5, 6, 4])
    print(res)
