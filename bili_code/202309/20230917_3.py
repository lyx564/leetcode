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
        self.res, self.pre = 99999999999, None

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            if self.pre:
                self.res = min(self.res, root.val - self.pre.val)
            self.pre = root
            in_order(root.right)
        in_order(root)
        return self.res


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    res = Solution().getMinimumDifference(root)
    print(res)