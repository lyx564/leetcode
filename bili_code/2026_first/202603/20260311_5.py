"""
968. 监控二叉树
给定一个二叉树，我们在树的节点上安装摄像头。
节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
计算监控树的所有节点所需的最小摄像头数量。

示例 1：
输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。

示例 2：
输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

https://leetcode.cn/problems/binary-tree-cameras/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root) -> int:
        self.res = 0

        def post_order(root):
            # 返回状态值：0（还没被拍），1（被其他监控拍了），2（自己装了摄像头）
            if not root:
                return 1 # 空节点，不需要拍，就等于被其他拍了，返回1
            left = post_order(root.left)
            right = post_order(root.right)
            if left == 1 and right == 1:
                return 0 # 叶子节点或者左右儿子都没有监控，所以还没被拍
            if left == 0 or right == 0:
                self.res += 1  # 左右儿子中至少有一个没被拍，需要在这里安监控
                return 2
            if left == 2 or right == 2:
                return 1  # 左右儿子中至少有一个有监控，已经被拍了，不需要对他安
        if post_order(root) == 0: # 根节点是叶子节点
            self.res += 1
        return self.res


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.left.left = TreeNode(0)
    root.left.left.left.right = TreeNode(0)
    res = Solution().minCameraCover(root)
    print(res)
