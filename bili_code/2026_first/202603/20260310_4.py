"""
135. 分发糖果
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
你需要按照以下要求，给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
相邻两个孩子中，评分更高的那个会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

示例 1：
输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。

示例 2：
输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。

https://leetcode.cn/problems/candy/description/
"""


class Solution:
    def candy(self, ratings) -> int:
        n = len(ratings)
        candy = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)
        return sum(candy)



if __name__ == '__main__':
    res = Solution().candy(ratings = [1,3,4,5,2])
    print(res)