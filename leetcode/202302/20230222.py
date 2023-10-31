"""
爱丽丝和鲍勃继续他们的石子游戏。许多堆石子排成一行，每堆都有正整数颗石子piles[i]。游戏以谁手中的石子最多来决出胜负。
爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，M = 1。
在每个玩家的回合中，该玩家可以拿走剩下的前X堆的所有石子，其中1 <= X <= 2M。然后，令M = max(M, X)。
游戏一直持续到所有石子都被拿走。
假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。

示例 1：
输入：piles = [2,7,9,4,4]
输出：10
解释：如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 = 10堆。如果Alice一开始拿走了两堆，那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。

示例 2:
输入：piles = [1,2,3,4,5,100]
输出：104

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/stone-game-ii
"""


class Solution:
    def stoneGameII(self, piles) -> int:
        n = len(piles)
        s = [0 for _ in range(n+1)]
        for i in range(n):
            s[i+1] = s[i] + piles[i]

        res_cache = {}

        def dfs(i, m):
            key = str(i) + '_' + str(m)
            if key in res_cache:
                return res_cache[key]
            if m * 2 >= n - i:
                res = s[n] - s[i]
            else:
                res = max(s[n] - s[i] - dfs(i + x, max(m, x)) for x in range(1, m*2+1))
            res_cache[key] = res
            return res
        return dfs(0, 1)


if __name__ == '__main__':
    res = Solution().stoneGameII(piles = [2,7,9,4,4])
    print(res)