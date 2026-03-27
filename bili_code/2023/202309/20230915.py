"""
106. 从中序与后序遍历序列构造二叉树
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

示例 1:
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]

示例 2:
输入：inorder = [-1], postorder = [-1]
输出：[-1]

https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        inorder_idx = inorder.index(root_val)
        root.left = self.buildTree(inorder[:inorder_idx], postorder[:inorder_idx])
        root.right = self.buildTree(inorder[inorder_idx + 1:], postorder[inorder_idx:-1])
        return root


if __name__ == '__main__':
    res = Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
    print(res)
