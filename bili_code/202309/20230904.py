"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l, r = head, head
        res = ListNode(-1)
        res.next = head
        for _ in range(n):
            r = r.next
        if not r:
            res.next = res.next.next
            return res.next
        while r.next:
            l = l.next
            r = r.next
        del_node = l.next
        l.next = l.next.next
        del del_node
        return res.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = Solution().removeNthFromEnd(head=head, n=5)
    while res:
        print(res.val)
        res = res.next