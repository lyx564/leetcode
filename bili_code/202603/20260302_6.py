"""
257. 二叉树的所有路径
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]

示例 2：
输入：root = [1]
输出：["1"]

https://leetcode.cn/problems/binary-tree-paths/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        self.res = []

        def dfs(node, history):
            if not node:
                return
            if not node.left and not node.right:
                self.res.append('->'.join(map(str, history)))
            if node.left:
                dfs(node.left, history + [node.left.val])
            if node.right:
                dfs(node.right, history + [node.right.val])

        dfs(root, [root.val])
        return self.res



if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.left = TreeNode(7)
    res = Solution().binaryTreePaths(root)
    print(res)