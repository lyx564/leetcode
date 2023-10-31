"""
有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从1 到n各不相同。
最开始时：

「一号」玩家从 [1, n]中取一个值x（1 <= x <= n）；
「二号」玩家也从[1, n]中取一个值y（1 <= y <= n）且y != x。
「一号」玩家给值为x的节点染上红色，而「二号」玩家给值为y的节点染上蓝色。

之后两位玩家轮流进行操作，「一号」玩家先手。每一回合，玩家选择一个被他染过色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色（「一号」玩家染红色，「二号」玩家染蓝色）。
如果（且仅在此种情况下）当前玩家无法找到这样的节点来染色时，其回合就会被跳过。
若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。
现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个y值可以确保你赢得这场游戏，则返回true ；若无法获胜，就请返回 false 。

示例 1 ：
输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
输出：true
解释：第二个玩家可以选择值为 2 的节点。

示例 2 ：
输入：root = [1,2,3], n = 3, x = 1
输出：false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-coloring-game
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.lnx = 0
        self.rnx = 0

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def dfs(root):
            if root is None:
                return 0
            ln, rn = dfs(root.left), dfs(root.right)
            if root.val == x:
                self.lnx, self.rnx = ln, rn

            return ln + rn + 1

        dfs(root)
        return max(self.lnx, self.rnx, n - self.lnx - self.rnx - 1) * 2 > n


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    res = Solution().btreeGameWinningMove(root=root, n=3, x=1)
    print(res)