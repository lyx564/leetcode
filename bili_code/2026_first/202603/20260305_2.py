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
        origin_root = root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif not root.left or not root.right:
            if root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None
        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
            return root
        return origin_root


    def deleteNode_1(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        origin_root = root
        last_node = None
        while root:
            if root.val < key:
                last_node = root
                root = root.right
            elif root.val > key:
                last_node = root
                root = root.left
            else:
                if not root.right:
                    if last_node:
                        if last_node.left == root:
                            last_node.left = root.left
                        if last_node.right == root:
                            last_node.right = root.left
                    else:
                        origin_root = root.left
                    return origin_root
                else:
                    last_node = root
                    successor = root.right
                    while successor.left:
                        last_node = successor
                        successor = successor.left
                    root.val = successor.val
                    if last_node != root:
                        last_node.left = successor.right
                    else:
                        last_node.right = successor.right
                    return origin_root

        return origin_root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    # root.left.left = TreeNode(2)
    # root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    res = Solution().deleteNode(root, key=5)

    print(res)
