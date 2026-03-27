"""
700. 二叉搜索树中的搜索
给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

示例 1:
输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]

示例 2:
输入：root = [4,2,7,1,3], val = 5
输出：[]

提示：
数中节点数在 [1, 5000] 范围内
1 <= Node.val <= 107
root 是二叉搜索树
1 <= val <= 107

https://leetcode.cn/problems/search-in-a-binary-search-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val: int):
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None

    def searchBST_1(self, root, val: int):
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST_1(root.left, val)
        else:
            return self.searchBST_1(root.right, val)

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    res = Solution().searchBST(root, 2)
    print(res)
