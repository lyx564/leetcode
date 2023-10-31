"""
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

示例 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder:
            return None
        val2idx = {}
        for i, val in enumerate(inorder):
            val2idx[val] = i
        length = len(preorder)

        def f(p_l, p_r, i_l, i_r):
            if p_l > p_r or i_l > i_r or p_r >= length or i_r >= length:
                return None
            val = preorder[p_l]
            root = TreeNode(val)
            in_idx = val2idx[val]
            root.left = f(p_l+1, p_l + in_idx - i_l, i_l, in_idx-1)
            root.right = f(p_l + in_idx - i_l + 1, p_r, in_idx+1, i_r)
            return root

        root = f(0, length-1, 0, length-1)
        return root


if __name__ == '__main__':
    res = Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
    # res = Solution().buildTree(preorder = [-1], inorder = [-1])
    print(res)