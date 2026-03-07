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

链接：https://leetcode.cn/problems/design-linked-list/description/
"""

class LinkNode:
    def __init__(self, val, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre


class MyLinkedList:

    def __init__(self):
        self.head = LinkNode(-1)

    def get(self, index: int) -> int:
        target_node = self.head
        for _ in range(index+1):
            if target_node.next is not None:
                target_node = target_node.next
            else:
                return -1
        return target_node.val

    def addAtHead(self, val: int) -> None:
        new_node = LinkNode(val)
        new_node.next = self.head.next
        new_node.pre = self.head
        if self.head.next is not None:
            self.head.next.pre = new_node
        self.head.next = new_node


    def addAtTail(self, val: int) -> None:
        new_node = LinkNode(val)
        tail_node = self.head
        while tail_node.next is not None:
            tail_node = tail_node.next
        tail_node.next = new_node
        new_node.pre = tail_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = LinkNode(val)
        target_node = self.head
        for _ in range(index):
            if target_node.next is not None:
                target_node = target_node.next
            else:
                return
        new_node.next = target_node.next
        if target_node.next:
            target_node.next.pre = new_node
        new_node.pre = target_node
        target_node.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        target_node = self.head
        for _ in range(index+1):
            if target_node.next is not None:
                target_node = target_node.next
            else:
                return
        if target_node.pre:
            target_node.pre.next = target_node.next
        if target_node.next:
            target_node.next.pre = target_node.pre




if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:

    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)
    myLinkedList.get(1)
    myLinkedList.deleteAtIndex(1)
    myLinkedList.get(1)