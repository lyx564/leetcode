"""
给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

限制：
1 ≤ k ≤ 二叉搜索树元素个数

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.path = 0
        self.res = 0

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.res = root.val
        def zhongxu(root: TreeNode, k):
            if not root:
                return
            if self.path == k:
                self.res = root.val
                return
            if self.path > k:
                return
            zhongxu(root.right, k)

            self.path += 1
            if k == self.path:
                self.res = root.val
                return
            zhongxu(root.left, k)
        zhongxu(root, k)
        return self.res


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.right = TreeNode(2)

    res = Solution().kthLargest(root=root, k=2)
    print(res)