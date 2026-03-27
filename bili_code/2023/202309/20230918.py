"""
501. 二叉搜索树中的众数
给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 任意顺序 返回。
假定 BST 满足如下定义：
结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树

示例 1：
输入：root = [1,null,2,2]
输出：[2]

示例 2：
输入：root = [0]
输出：[0]

提示：
树中节点的数目在范围 [1, 104] 内
-105 <= Node.val <= 105

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode):
        self.last_node, self.fre = None, 0
        self.res, self.max_fre = [], 0

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            if not self.last_node:
                self.fre = 1
            else:
                if self.last_node.val != root.val:
                    if self.fre > self.max_fre:
                        self.res = [self.last_node.val]
                        self.max_fre = self.fre
                    elif self.fre == self.max_fre:
                        self.res.append(self.last_node.val)
                    self.fre = 1
                else:
                    self.fre += 1
            self.last_node = root
            in_order(root.right)

        in_order(root)
        if self.fre > self.max_fre:
            self.res = [self.last_node.val]
        elif self.fre == self.max_fre:
            self.res.append(self.last_node.val)
        return self.res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    # root.right.left = TreeNode(2)
    res = Solution().findMode(root)
    print(res)
