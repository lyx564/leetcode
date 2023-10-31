"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class MaxQueue:

    def __init__(self):
        self.queue = []
        self.max_queue = []

    def max_value(self) -> int:
        if self.max_queue:
            return self.max_queue[0]
        return -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue = self.max_queue[:-1]
        self.max_queue.append(value)
        print('push', value)
        print(self.queue)
        print(self.max_queue)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        res = self.queue[0]
        self.queue = self.queue[1:]
        if res == self.max_queue[0]:
            self.max_queue = self.max_queue[1:]
        print('pop')
        print(self.queue)
        print(self.max_queue)

        return res


if __name__ == '__main__':

    # Your MaxQueue object will be instantiated and called as such:
    obj = MaxQueue()
    param_1 = obj.max_value()
    # print(param_1)
    obj.push_back(15)
    param_1 = obj.max_value()
    # print(param_1)
    obj.push_back(9)
    param_1 = obj.max_value()
    # print(param_1)
    obj.push_back(4)
    param_1 = obj.max_value()
    # print(param_1)
    param_3 = obj.pop_front()
    # print(param_3)
    param_3 = obj.pop_front()