"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead","deleteHead"]
[[],[3],[],[],[]]
输出：[null,null,3,-1,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack1 and not self.stack2:
            return -1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1[-1])
                self.stack1 = self.stack1[:-1]
        res = self.stack2[-1]
        self.stack2 = self.stack2[:-1]
        return res


if __name__ == '__main__':
    # Your CQueue object will be instantiated and called as such:
    obj = CQueue()
    print(obj.deleteHead())
    print(obj.appendTail(5))
    print(obj.appendTail(2))
    print(obj.deleteHead())
    print(obj.deleteHead())