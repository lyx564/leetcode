"""
101. 对称二叉树
给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false

提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100

进阶：你可以运用递归和迭代两种方法解决这个问题吗？

https://leetcode.cn/problems/symmetric-tree/description/

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def digui(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2:
                if root1.val != root2.val:
                    return False
                if digui(root1.left, root2.right) and digui(root1.right, root2.left):
                    return True
            return False

        res = digui(root.left, root.right)

        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    res = Solution().isSymmetric_1(root)
    print(res)

