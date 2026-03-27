"""
203. 移除链表元素
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]

提示：
列表中的节点数目在范围 [0, 104] 内
1 <= Node.val <= 50
0 <= val <= 50

链接：https://leetcode.cn/problems/remove-linked-list-elements/submissions/692263044/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result_head = head
        while result_head is not None and result_head.val == val:
            result_head = result_head.next
        if result_head is None:
            return None
        last_node, now_node = result_head, result_head.next
        while now_node is not None:
            while now_node is not None and now_node.val != val:
                last_node, now_node = now_node, now_node.next
            while now_node is not None and now_node.val == val:
                del_node = now_node
                now_node = now_node.next
                del del_node

            last_node.next = now_node

        return result_head


if __name__ == '__main__':
    node = ListNode(val=1)
    node.next = ListNode(val=2)
    node.next.next = ListNode(val=6)
    node.next.next.next = ListNode(val=3)
    node.next.next.next.next = ListNode(val=4)
    node.next.next.next.next.next = ListNode(val=5)
    node.next.next.next.next.next.next = ListNode(val=6)
    # node = ListNode(val=7)
    # node.next = ListNode(val=7)
    # node.next.next = ListNode(val=7)
    # node.next.next.next = ListNode(val=7)
    res = Solution().removeElements(node, val=6)
    while res is not None:
        print(res.val)
        res = res.next

