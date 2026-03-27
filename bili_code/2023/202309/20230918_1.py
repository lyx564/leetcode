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
        self.res_path = []

        def dfs(root, target, path):
            print(self.history)
            if not root or len(self.res_path) == 2 or root.val in self.history:
                return
            self.history.add(root.val)
            if root == target:
                self.res_path.append(path + [root.val])
            else:
                dfs(root.left, target, path + [root.val])
                dfs(root.right, target, path + [root.val])

        dfs(root, p, [])
        dfs(root, q, [])
        print(self.res_path)
        i = 0
        path1, path2 = self.res_path[0], self.res_path[1]
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i += 1
        return path1[i - 1]

    def lowestCommonAncestor_2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.father = {root.val: None}

        def dfs(root):
            if not root:
                return
            if root.left:
                self.father[root.left.val] = root
                dfs(root.left)
            if root.right:
                self.father[root.right.val] = root
                dfs(root.right)

        dfs(root)
        p_path = set()

        while p and p.val in self.father:
            p_path.add(p.val)
            p = self.father[p.val]
        while q and q.val not in p_path and q.val in self.father:
            q = self.father[q.val]
        return q

    def lowestCommonAncestor_3(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_val, q_val = p.val, q.val
        self.res = None

        def post_order(root):
            if not root or self.res:
                return False
            if_left = post_order(root.left)
            if_right = post_order(root.right)

            if if_left or if_right:
                if if_left and if_right:
                    self.res = root
                if root.val == p_val or root.val == q_val:
                    self.res = root
                return True
            if root.val == p_val or root.val == q_val:
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
    res = Solution().lowestCommonAncestor_3(root, root.left, root.left.left.right)
    print(res.val)
