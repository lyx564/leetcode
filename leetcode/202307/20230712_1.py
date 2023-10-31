"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2

给定的树 B：
   4
  /
 1

返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False

        def f(A, B, rootB):
            if B is None:
                return True
            if A is None:
                return False
            if A.val == B.val:
                if not B.left and not B.right:
                    return True
                left_shot = f(A.left, B.left, rootB)
                right_shot = f(A.right, B.right, rootB)
                if left_shot and right_shot:
                    return True
            return f(A.left, rootB, rootB) or f(A.right, rootB, rootB)
        return f(A, B, B)


if __name__ == '__main__':
    rootA = TreeNode(4)
    rootA.left = TreeNode(2)
    rootA.right = TreeNode(3)
    rootA.left.left = TreeNode(-4)
    rootA.left.right = TreeNode(-3)
    rootA.left.right = TreeNode(-3)
    rootA.left.right = TreeNode(-3)

    rootB = TreeNode(-2)
    rootB.left = TreeNode(1)
    rootB.right = TreeNode(-2)
    res = Solution().isSubStructure(rootA, rootB)
    print(res)

