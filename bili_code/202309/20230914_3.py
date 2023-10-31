"""
222. 完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例 1：
输入：root = [1,2,3,4,5,6]
输出：6

示例 2：
输入：root = []
输出：0

示例 3：
输入：root = [1]
输出：1

提示：树中节点的数目范围是[0, 5 * 104]
0 <= Node.val <= 5 * 104
题目数据保证输入的树是 完全二叉树

进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0

        def if_all_tree(root):
            if not root:
                return True, 0
            left_h, right_h = 0, 0
            left, right = root.left, root.right
            while left:
                left_h += 1
                left = left.left
            while right:
                right_h += 1
                right = right.right
            if left_h == right_h:
                return True, left_h+1
            return False, 0
        left, right = root.left, root.right
        if_left, left_h = if_all_tree(left)
        if_right, right_h = if_all_tree(right)
        if if_left:
            left_num = pow(2, left_h) - 1
        else:
            left_num = 1 + self.countNodes(left.left) + self.countNodes(left.right)

        if if_right:
            right_num = pow(2, right_h) - 1
        else:
            right_num = 1 + self.countNodes(right.left) + self.countNodes(right.right)

        return 1 + left_num + right_num






if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    res = Solution().countNodes(root=root)
    print(res)