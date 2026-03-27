"""
513. 找树左下角的值
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
假设二叉树中至少有一个节点。

示例 1:
输入: root = [2,1,3]
输出: 1

示例 2:
输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7

提示:

二叉树的节点个数的范围是 [1,104]
-231 <= Node.val <= 231 - 1

https://leetcode.cn/problems/find-bottom-left-tree-value/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.max_depth, self.res = 1, root.val

        def dfs(root, now_depth):
            if not root:
                return
            if self.max_depth < now_depth:
                self.res = root.val
                self.max_depth += 1
            dfs(root.left, now_depth+1)
            dfs(root.right, now_depth+1)
        dfs(root, 1)
        return self.res

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    res = Solution().findBottomLeftValue(root)
    print(res)