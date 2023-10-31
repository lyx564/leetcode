"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

https://leetcode.cn/problems/permutations-ii/

"""

class Solution:
    def permuteUnique(self, nums):

        res = []

        def digui(lists, now_res):
            if len(now_res) == len(nums):
                res.append(now_res)
                return
            history = set()
            for i in range(len(lists)):
                if lists[i] in history:
                    continue
                history.add(lists[i])
                digui(lists[:i] + lists[i+1:], now_res + [lists[i]])
        digui(nums, [])
        return res


if __name__ == '__main__':
    res = Solution().permuteUnique(nums=[1, 1, 3, 1])
    print(res)