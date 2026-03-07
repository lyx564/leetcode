"""
98. 验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1：
输入：root = [2,1,3]
输出：true

示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4

https://leetcode.cn/problems/validate-binary-search-tree/

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if node.val >= max_val or node.val <= min_val:
                return False
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, -float('inf'), float('inf'))

    def isValidBST_1(self, root: TreeNode) -> bool:
        if not root:
            return True

        self.now_num = -float('inf')
        def mid_order(node):
            left_res = True
            if node.left:
                left_res = mid_order(node.left)
            if node.val <= self.now_num:
                return False
            self.now_num = node.val
            right_res = True
            if node.right:
                right_res = mid_order(node.right)
            return left_res and right_res

        return mid_order(root)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    res = Solution().isValidBST(root)
    print(res)