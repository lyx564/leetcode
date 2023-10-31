"""
给你两个二维整数数组items1 和items2，表示两个物品集合。每个数组items有以下特质：
items[i] = [valuei, weighti] 其中valuei表示第i件物品的价值，weighti表示第 i件物品的 重量。
items中每件物品的价值都是 唯一的。
请你返回一个二维数组ret，其中ret[i] = [valuei, weighti]，weighti是所有价值为valuei物品的重量之和。
注意：ret应该按价值 升序排序后返回。

示例 1：
输入：items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
输出：[[1,6],[3,9],[4,5]]
解释：
value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 5 ，总重量为 1 + 5 = 6 。
value = 3 的物品再 items1 中 weight = 8 ，在 items2 中 weight = 1 ，总重量为 8 + 1 = 9 。
value = 4 的物品在 items1 中 weight = 5 ，总重量为 5 。
所以，我们返回 [[1,6],[3,9],[4,5]] 。

示例 2：
输入：items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
输出：[[1,4],[2,4],[3,4]]
解释：
value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 3 ，总重量为 1 + 3 = 4 。
value = 2 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 1 ，总重量为 3 + 1 = 4 。
value = 3 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。
所以，我们返回 [[1,4],[2,4],[3,4]] 。

示例 3：
输入：items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]
输出：[[1,7],[2,4],[7,1]]
解释：
value = 1 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 4 ，总重量为 3 + 4 = 7 。
value = 2 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。
value = 7 的物品在 items2 中 weight = 1 ，总重量为 1 。
所以，我们返回 [[1,7],[2,4],[7,1]] 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-similar-items
"""


class Solution:
    def mergeSimilarItems(self, items1, items2):
        res_dic = {}
        for v, w in items1 + items2:
            if v in res_dic:
                res_dic[v] += w
            else:
                res_dic[v] = w
        res = [[v, res_dic[v]] for v in res_dic.keys()]
        res.sort(key=lambda x: x[0], reverse=False)
        return res


if __name__ == '__main__':
    res = Solution().mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]])
    print(res)
