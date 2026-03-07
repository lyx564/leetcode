"""
102. 二叉树的层序遍历
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]

https://leetcode.cn/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [[root, 1]]
        while queue:
            curr = queue[0]
            node, level = curr[0], curr[1]
            while level > len(res):
                res.append([])
            res[level-1].append(node.val)
            left, right = node.left, node.right
            if left:
                queue.append([left, level+1])
            if right:
                queue.append([right, level+1])
            queue = queue[1:]
        return res


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    res = Solution().levelOrder(root)
    print(res)
