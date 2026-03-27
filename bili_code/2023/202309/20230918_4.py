"""
450. 删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。

示例 1:
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。


示例 2:

输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点
示例 3:

输入: root = [], key = 0
输出: []

https://leetcode.cn/problems/delete-node-in-a-bst/

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif not root.left or not root.right:
            return root.left if root.left else root.right
        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            successor.right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            return successor
        return root



    def deleteNode_1(self, root: TreeNode, key: int) -> TreeNode:

        def delete_root(root):
            origin_root = root
            if not root.left and not root.right:
                return None
            if root.left:
                root = root.left
                if root.right:
                    last_node = root
                    while root.right:
                        last_node = root
                        root = root.right
                    origin_root.val = root.val
                    last_node.right = root.left
                    del root
                    return origin_root
                else:
                    root.right = origin_root.right
                    del origin_root
                    return root
            else:
                root = root.right
                if root.left:
                    last_node = root
                    while root.left:
                        last_node = root
                        root = root.left
                    origin_root.val = root.val
                    last_node.left = root.right
                    del root
                    return origin_root
                else:
                    root.left = origin_root.left
                    del origin_root
                    return root
        if not root:
            return None
        res = root
        last_node = None
        if root.val == key:
            return delete_root(root)

        while root and root.val != key:
            last_node = root
            if root.val > key:
                root = root.left
            else:
                root = root.right
        if not root:
            return res

        if key > last_node.val:
            last_node.right = delete_root(root)
        else:
            last_node.left = delete_root(root)

        return res

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right = TreeNode(7)
    # root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    res = Solution().deleteNode(root, key=3)

    print(res)
