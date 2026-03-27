"""
24. 两两交换链表中的节点
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/swap-nodes-in-pairs/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = head
        if p is None or p.next is None:
            return p
        fake_head = ListNode(-1)
        fake_head.next = p.next
        l = fake_head

        while p is not None:
            q = p.next
            if q is not None:
                l.next = q
                r = q.next
                q.next = p
                p.next = r
            l = p
            p = p.next

        return fake_head.next




if __name__ == '__main__':
    node = ListNode(1)
    # node.next = ListNode(2)
    # node.next.next = ListNode(3)
    # node.next.next.next = ListNode(4)
    # node.next.next.next.next = ListNode(5)
    res = Solution().swapPairs(node)
    while res:
        print(res.val)
        res = res.next
