"""
给你一棵 完整二叉树的根，这棵树有以下特征：

叶子节点要么值为0要么值为1，其中0 表示False，1 表示True。
非叶子节点 要么值为 2要么值为 3，其中2表示逻辑或OR ，3表示逻辑与AND。
计算一个节点的值方式如下：

如果节点是个叶子节点，那么节点的 值为它本身，即True或者False。
否则，计算两个孩子的节点值，然后将该节点的运算符对两个孩子值进行 运算。
返回根节点root的布尔运算值。

完整二叉树是每个节点有 0个或者 2个孩子的二叉树。
叶子节点是没有孩子的节点。

示例 1：
输入：root = [2,1,3,null,null,0,1]
输出：true
解释：上图展示了计算过程。
AND 与运算节点的值为 False AND True = False 。
OR 运算节点的值为 True OR False = True 。
根节点的值为 True ，所以我们返回 true 。

示例 2：
输入：root = [0]
输出：false
解释：根节点是叶子节点，且值为 false，所以我们返回 false 。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/evaluate-boolean-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root) -> bool:
        if root.val == 0 or root.val == 1:
            return root.val == 1
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        if root.val == 2:
            return l or r
        if root.val == 3:
            return l and r
        return True


if __name__ == '__main__':
    root = TreeNode(0)
    # root.left = TreeNode(1)
    # root.right = TreeNode(3)
    # root.right.left = TreeNode(0)
    # root.right.right = TreeNode(1)
    res = Solution().evaluateTree(root)
    print(res)
