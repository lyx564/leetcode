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

提示:

节点数在 [1, 1000] 范围内
-1000 <= Node.val <= 1000

https://leetcode.cn/problems/sum-of-left-leaves/description/

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            left_sum = root.left.val
        else:
            left_sum = self.sumOfLeftLeaves(root.left)
        right_sum = self.sumOfLeftLeaves(root.right)
        return left_sum + right_sum



if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    res = Solution().sumOfLeftLeaves(root)
    print(res)