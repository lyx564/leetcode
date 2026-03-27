"""
104. 二叉树的最大深度
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3

示例 2：
输入：root = [1,null,2]
输出：2

https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        def dfs(node, depth):
            if not node:
                return depth
            left_depth = dfs(node.left, depth+1)
            right_depth = dfs(node.right, depth+1)
            res = max(left_depth, right_depth)
            return res
        res = dfs(root, 0)
        return res


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    res = Solution().maxDepth(root)
    print(res)
