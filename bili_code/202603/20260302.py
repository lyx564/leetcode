"""
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回 它的 中序 遍历

https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [[root, 0]]
        while stack:
            node = stack[-1]
            if node[1] == 0 and node[0].left:
                stack[-1][1] = 1
                stack.append([node[0].left, 0])
            elif node[1] == 1 or node[0].left is None:
                res.append(node[0].val)
                stack = stack[:-1]
                if node[0].right:
                    stack.append([node[0].right, 0])
        return res

    def inorderTraversal_1(self, root):
        if not root:
            return []
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

    def inorderTraversal_2(self, root):
        if not root:
            return []
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            res.append(curr.val)
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
    res = Solution().inorderTraversal_2(root)
    print(res)

