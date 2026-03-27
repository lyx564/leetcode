"""
530. 二叉搜索树的最小绝对差
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
差值是一个正数，其数值等于两值之差的绝对值。

示例 1：
输入：root = [4,2,6,1,3]
输出：1

示例 2：
输入：root = [1,0,48,null,null,12,49]
输出：1

https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = 999999999999
        self.last_val = -9999999999
        def mid_order(node):
            if not node:
                return
            mid_order(node.left)
            if abs(node.val - self.last_val) < self.res:
                self.res = abs(node.val - self.last_val)
            self.last_val = node.val
            mid_order(node.right)

        mid_order(root)
        return self.res


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    res = Solution().getMinimumDifference(root)
    print(res)