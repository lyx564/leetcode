"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true

提示：

数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def verifyPostorder_1(self, postorder) -> bool:
        if not postorder:
            return True
        root = postorder[-1]
        left_tree, right_tree = [], []
        i = len(postorder) - 2
        while i >= 0 and postorder[i] > root:
            right_tree = [postorder[i]] + right_tree
            i -= 1
        while i >= 0 and postorder[i] < root:
            left_tree = [postorder[i]] + left_tree
            i -= 1
        if len(left_tree) + len(right_tree) != len(postorder) - 1:
            return False
        return self.verifyPostorder_1(left_tree) and self.verifyPostorder_1(right_tree)

    def verifyPostorder_2(self, postorder) -> bool:
        if not postorder:
            return True
        root = 9999999
        stack = []
        for i in range(len(postorder)-1, -1, -1):
            print(i, root, stack)
            if postorder[i] > root:
                return False
            while stack and stack[-1] > postorder[i]:
                root = stack[-1]
                stack = stack[:-1]

            stack.append(postorder[i])
        return True


if __name__ == '__main__':
    res = Solution().verifyPostorder_2([1,3,2,6,5])
    print(res)

