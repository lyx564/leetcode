"""
请实现两个函数，分别用来序列化和反序列化二叉树。
你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

示例：
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return '[]'
        quene = collections.deque()
        quene.append(root)
        while quene:
            node = quene.popleft()
            if node:
                quene.append(node.left)
                quene.append(node.right)
                res.append(str(node.val))
            else:
                res.append('N')
        return '[' + '|'.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = data[1:-1].split('|')
        root = TreeNode(int(data[0]))
        quene = collections.deque()
        quene.append(root)
        pos = 1
        while quene:
            node = quene.popleft()
            if data[pos] != 'N':
                node.left = TreeNode(int(data[pos]))
                quene.append(node.left)
            pos += 1
            if data[pos] != 'N':
                node.right = TreeNode(int(data[pos]))
                quene.append(node.right)
            pos += 1
        return root


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec()
    code = codec.serialize(root)
    tree = codec.deserialize(code)
    print(code)