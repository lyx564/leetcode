"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        r = res
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        if l1:
            res.next = l1
        elif l2:
            res.next = l2
        return r.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(4)
    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)
    res = Solution().mergeTwoLists(node1, node2)
    while res:
        print(res.val)
        res = res.next