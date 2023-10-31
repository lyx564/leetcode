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

提示：

树中节点的数目在范围 [1, 100] 内
-100 <= Node.val <= 100

https://leetcode.cn/problems/binary-tree-paths/

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        res = []
        def digui(root, path):
            if not root.left and not root.right:
                res.append('->'.join([str(x) for x in path + [root.val]]))
                return
            if root.left:
                digui(root.left, path+[root.val])
            if root.right:
                digui(root.right, path+[root.val])
        digui(root, [])
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    res = Solution().binaryTreePaths(root)
    print(res)