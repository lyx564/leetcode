"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]


提示：
节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/?envType=study-plan-v2&envId=coding-interviews
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
            node, level = quene[0][0], quene[0][1]
            if node.left:
                quene.append([node.left, level+1])
            if node.right:
                quene.append([node.right, level+1])
            quene = quene[1:]
            if len(res) == level:
                if level % 2 == 1:
                    res[-1].append(node.val)
                else:
                    res[-1] = [node.val] + res[-1]
            else:
                res.append([node.val])
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = Solution().levelOrder(root)
    print(res)