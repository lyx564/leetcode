"""
222. 完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
若最底层为第 h 层（从第 0 层开始），则该层包含 1~ 2h 个节点。

示例 1：
输入：root = [1,2,3,4,5,6]
输出：6

示例 2：
输入：root = []
输出：0

示例 3：
输入：root = [1]
输出：1

https://leetcode.cn/problems/count-complete-tree-nodes/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        left_height = 0
        node = root
        while node:
            node = node.left
            left_height += 1
        right_height = 0
        node = root
        while node:
            node = node.right
            right_height += 1
        if left_height == right_height:
            return 2 ** left_height - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.left = TreeNode(7)
    res = Solution().countNodes(root)
    print(res)

