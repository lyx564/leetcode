"""
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1

提示：

树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。

https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p_path, self.q_path = [], []
        def dfs(node, path):
            if not node:
                return
            if self.p_path and self.q_path:
                return
            if node == p:
                self.p_path = path+[node]
            elif node == q:
                self.q_path = path+[node]
            dfs(node.left, path+[node])
            dfs(node.right, path+[node])
        dfs(root, [])
        i = 0
        while i < len(self.q_path) and i < len(self.p_path) and self.p_path[i] == self.q_path[i]:
            i += 1
        return self.q_path[i-1]

    def lowestCommonAncestor_1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        def post_order(node):
            if not node:
                return False
            l_exist = post_order(node.left)
            r_exist = post_order(node.right)
            if l_exist is True and r_exist is True:
                self.res = node
                return True
            if (l_exist or r_exist) and (node == p or node == q):
                self.res = node
                return True
            if l_exist is True or r_exist is True:
                return True
            if p == node or q == node:
                return True
            return False
        post_order(root)
        return self.res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(8)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    res = Solution().lowestCommonAncestor_1(root, root.left, root.left.left.right)
    print(res.val)
