"""
404. 左叶子之和
给定二叉树的根节点 root ，返回所有左叶子之和。

示例 1：
输入: root = [3,9,20,null,null,15,7]
输出: 24
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

示例 2:
输入: root = [1]
输出: 0

https://leetcode.cn/problems/sum-of-left-leaves/description/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        self.res = 0

        def dfs(node, direction):
            if not node:
                return
            if not node.left and not node.right:
                if direction == 'left':
                    self.res += node.val
            dfs(node.left, 'left')
            dfs(node.right, 'right')
        dfs(root, '')
        return self.res


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.left = TreeNode(7)
    res = Solution().sumOfLeftLeaves(root)
    print(res)