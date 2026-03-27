"""
110. 平衡二叉树
给定一个二叉树，判断它是否是 平衡二叉树

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：true

示例 2：
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

示例 3：
输入：root = []
输出：true

https://leetcode.cn/problems/balanced-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        self.res = True
        def dfs(node, depth):
            if not node:
                return depth
            left_depth = dfs(node.left, depth+1)
            right_depth = dfs(node.right, depth+1)
            if abs(left_depth - right_depth) > 1:
                self.res = False
            return max(left_depth, right_depth)

        dfs(root, 0)
        return self.res


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.left = TreeNode(7)
    root.right.left.left = TreeNode(7)
    root.right.left.left.left = TreeNode(7)
    res = Solution().isBalanced(root)
    print(res)