"""
1. 二叉树 中序遍历 非递归
2. n个骰子， 输出骰子和为n-6n的概率分布

"""

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
def f1(root):
    res = []
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        now = stack[-1]
        stack = stack[:-1]
        res.append(now.val)
        root = now.right

    return res


def f2(n):

    dp = [[0 for _ in range(6*n+1)] for _ in range(n+1)]

    for j in range(1, 7):
        dp[1][j] = 1/6

    for i in range(2, n+1):
        for j in range(i, 6*i+1):
            for k in range(max(1, j-6), j):
                dp[i][j] += dp[i-1][k]
            dp[i][j] *= (1/6)

    return dp[n]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(f1(root))

    print(f2(1))
    print(f2(2))
    print(f2(3))