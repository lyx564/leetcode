"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

https://leetcode.cn/problems/minimum-depth-of-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        self.res = 99999

        def dfs(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.res = min(self.res, depth)
                return
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return self.res


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    res = Solution().minDepth(root)
    print(res)
