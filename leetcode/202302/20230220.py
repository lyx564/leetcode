"""
给你一个整数数组ranks和一个字符数组suit。你有5张扑克牌，第i张牌大小为ranks[i]，花色为suits[i]。
下述是从好到坏你可能持有的 手牌类型：

"Flush"：同花，五张相同花色的扑克牌。
"Three of a Kind"：三条，有 3 张大小相同的扑克牌。
"Pair"：对子，两张大小一样的扑克牌。
"High Card"：高牌，五张大小互不相同的扑克牌。
请你返回一个字符串，表示给定的 5 张牌中，你能组成的 最好手牌类型。

注意：返回的字符串大小写需与题目描述相同。
示例 1：
输入：ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
输出："Flush"
解释：5 张扑克牌的花色相同，所以返回 "Flush" 。

示例 2：
输入：ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
输出："Three of a Kind"
解释：第一、二和四张牌组成三张相同大小的扑克牌，所以得到 "Three of a Kind" 。
注意我们也可以得到 "Pair" ，但是 "Three of a Kind" 是更好的手牌类型。
有其他的 3 张牌也可以组成 "Three of a Kind" 手牌类型。

示例 3：
输入：ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
输出："Pair"
解释：第一和第二张牌大小相同，所以得到 "Pair" 。
我们无法得到 "Flush" 或者 "Three of a Kind" 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/best-poker-hand
"""

class Solution:
    def bestHand(self, ranks, suits) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        count = {}
        for r in ranks:
            if r not in count:
                count[r] = 1
            else:
                count[r] += 1
                if count[r] > 2:
                    return 'Three of a Kind'
        if len(set(ranks)) <= len(ranks) - 1:
            return 'Pair'
        return 'High Card'


if __name__ == '__main__':
    res = Solution().bestHand(ranks = [2,10,7,10,7], suits = ["a","b","a","d","b"])
    print(res)