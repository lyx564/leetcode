"""
707. 设计链表
你可以选择使用单链表或者双链表，设计并实现自己的链表。
单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。
如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。

实现 MyLinkedList 类：
MyLinkedList() 初始化 MyLinkedList 对象。
int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。

示例：
输入
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
输出
[null, null, null, null, 2, null, 3]

解释
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
myLinkedList.get(1);              // 返回 2
myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
myLinkedList.get(1);              // 返回 3

提示：
0 <= index, val <= 1000
请不要使用内置的 LinkedList 库。
调用 get、addAtHead、addAtTail、addAtIndex 和 deleteAtIndex 的次数不超过 2000 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/design-linked-list/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        node = self.head
        while node and index > 0:
            node = node.next
            index -= 1
        if node:
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = LinkNode(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = LinkNode(val)
        now_node = self.head
        if not now_node:
            self.head = node
            return
        while now_node.next:
            now_node = now_node.next
        now_node.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        new_node = LinkNode(val)
        node = self.head
        while node and index > 1:
            node = node.next
            index -= 1
        if not node:
            return
        new_node.next = node.next
        node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        node = self.head
        if index == 0:
            self.head = node.next
            del node
            return
        while node and node.next and index > 1:
            node = node.next
            index -= 1
        if not node or not node.next:
            return
        del_node = node.next
        node.next = node.next.next
        del del_node


if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    obj.addAtHead(2)
    obj.deleteAtIndex(1)
    obj.addAtHead(2)
    obj.addAtHead(7)
    obj.addAtHead(3)
    obj.addAtHead(2)
    obj.addAtHead(5)
    obj.addAtTail(5)
    param_1 = obj.get(5)
    obj.deleteAtIndex(6)
    obj.deleteAtIndex(4)
    print()