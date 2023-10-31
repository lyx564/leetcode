"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [9999]

    def push(self, x: int) -> None:
        self.stack.append(x)
        min_val = min(x, self.min_stack[-1])
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.min())
    minStack.pop()
    print(minStack.top())
    print(minStack.min())
