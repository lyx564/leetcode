"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        l, p, q = ListNode(-1), head, head.next
        l.next = None
        while q:
            p.next = l.next
            l.next = p
            p = q
            q = q.next
        p.next = l.next
        return p


if __name__ == '__main__':

    node = ListNode(1) #
    node.next = ListNode(2) # l
    node.next.next = ListNode(3) # p
    node.next.next.next = ListNode(4) #q
    node.next.next.next.next = ListNode(5)
    res = Solution().reverseList(node)
    while res:
        print(res.val)
        res = res.next