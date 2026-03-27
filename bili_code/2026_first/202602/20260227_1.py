"""
144. 二叉树的后序遍历
给你二叉树的根节点 root ，返回它节点值的 后序 遍历。
https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        curr, stack = root, []
        while curr or stack:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            curr = stack[-1]
            stack = stack[:-1]
            curr = curr.left
        return res[::-1]

    def postorderTraversal_1(self, root):
        if not root:
            return []
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        dfs(root)
        return res

    def postorderTraversal_2(self, root):
        if not root:
            return []
        res = []
        stack = [[root, 0]]
        while stack:
            node = stack[-1]
            left, right = node[0].left, node[0].right
            if node[1] == 0:
                node[1] = 1
                if right:
                    stack.append([right, 0])
                if left:
                    stack.append([left, 0])
            elif node[1] == 1 or (not left and not right):
                res.append(node[0].val)
                stack = stack[:-1]
        return res







if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    res = Solution().postorderTraversal_2(root)
    print(res)
