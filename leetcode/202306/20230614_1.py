"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树:[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        quene = [[root, 1]]
        res = [[]]
        while quene:
            now_node, now_level = quene[0]
            if now_node.left:
                quene.append([now_node.left, now_level+1])
            if now_node.right:
                quene.append([now_node.right, now_level + 1])
            quene = quene[1:]
            if len(res) < now_level:
                res.append([now_node.val])
            else:
                res[-1].append(now_node.val)
        return res


if __name__ == '__main__':
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    res = Solution().levelOrder(node)
    print(res)