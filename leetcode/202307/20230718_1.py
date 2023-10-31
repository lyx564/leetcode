"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def findContinuousSequence(self, target: int):
        res = []
        target *= 2
        i = target // 2
        while i > 1:
            if target % i == 0:
                sum = target // i
                if (sum+1-i) % 2 != 0:
                    i -= 1
                    continue
                start = (sum+1-i) // 2
                if start <= 0:
                    i -= 1
                    continue
                res.append([x for x in range(start, sum-start+1)])
            i -= 1
        return res

    def findContinuousSequence_1(self, target: int):
        res = []
        i, j = 1, 1
        sum = 1
        while i <= j <= target // 2:
            while sum < target:
                j += 1
                sum += j
            while sum > target:
                sum -= i
                i += 1
            if sum == target:
                res.append([x for x in range(i, j+1)])
                sum -= i
                i += 1
        return res


if __name__ == '__main__':
    res = Solution().findContinuousSequence_1(target = 15)
    print(res)