"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]

示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]

限制：
最多会对 addNum、findMedian 进行 50000 次调用。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.data)-1
        mid = 0
        while l < r:
            mid = (l + r) // 2
            data_num = self.data[mid]
            if data_num == num:
                l = mid
                break
            elif data_num > num:
                r = mid - 1
            else:
                l = mid + 1
        if l < len(self.data) and self.data[l] < num:
            l += 1
        self.data = self.data[:l] + [num] + self.data[l:]
        print(self.data)

    def findMedian(self) -> float:
        len_data = len(self.data)
        mid = len_data // 2
        if len_data % 2 == 1:
            return self.data[mid]
        return (self.data[mid - 1] + self.data[mid]) / 2


class MedianFinder_1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.data)-1
        mid = 0
        while l < r:
            mid = (l + r) // 2
            data_num = self.data[mid]
            if data_num == num:
                l = mid
                break
            elif data_num > num:
                r = mid - 1
            else:
                l = mid + 1
        if l < len(self.data) and self.data[l] < num:
            l += 1
        self.data = self.data[:l] + [num] + self.data[l:]
        print(self.data)

    def findMedian(self) -> float:
        len_data = len(self.data)
        mid = len_data // 2
        if len_data % 2 == 1:
            return self.data[mid]
        return (self.data[mid - 1] + self.data[mid]) / 2


if __name__ == '__main__':
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    obj.addNum(12)
    print(obj.findMedian())
    obj.addNum(10)
    print(obj.findMedian())
    obj.addNum(13)
    print(obj.findMedian())
    obj.addNum(11)
    print(obj.findMedian())
    obj.addNum(5)
    print(obj.findMedian())
    obj.addNum(15)
    print(obj.findMedian())
    obj.addNum(1)
    print(obj.findMedian())
    obj.addNum(11)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(17)
    print(obj.findMedian())
    obj.addNum(14)
    print(obj.findMedian())
