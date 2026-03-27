"""
144. 二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            res.append(stack[-1].val)
            left = stack[-1].left
            right = stack[-1].right
            stack = stack[:-1]
            if right:
                stack.append(right)
            if left:
                stack.append(left)
        return res

    def preorderTraversal_1(self, root):
        if not root:
            return []
        res = []

        def dfs(root):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    def preorderTraversal_2(self, root):
        if not root:
            return []
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            stack = stack[:-1]
            curr = curr.right
        return res






if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    res = Solution().preorderTraversal_2(root)
    print(res)

