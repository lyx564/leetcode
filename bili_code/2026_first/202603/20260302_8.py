"""
513. 找树左下角的值
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
假设二叉树中至少有一个节点。

示例 1:
输入: root = [2,1,3]
输出: 1

示例 2:
输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
https://leetcode.cn/problems/find-bottom-left-tree-value/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root):
        self.res = 0
        self.max_depth = 0

        def dfs(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                if depth > self.max_depth:
                    self.res = node.val
                    self.max_depth = depth
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 1)
        return self.res





if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.left = TreeNode(7)
    res = Solution().findBottomLeftValue(root)
    print(res)