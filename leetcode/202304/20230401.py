"""
1019. 链表中的下一个更大节点
给定一个长度为n的链表head
对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。
返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。如果第 i 个节点没有下一个更大的节点，设置answer[i] = 0。

示例 1：
输入：head = [2,1,5]
输出：[5,5,0]

示例 2：
输入：head = [2,7,4,3,5]
输出：[7,0,5,5,0]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/next-greater-node-in-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode):
        res = []
        stack = [[head.val, 0]]
        head = head.next
        while head:
            res.append(0)
            idx = stack[-1][1] + 1
            while stack and head.val > stack[-1][0]:
                pop = stack[-1]
                res[pop[1]] = head.val
                stack = stack[:-1]

            stack.append([head.val, idx])
            head = head.next

        return res + [0]


if __name__ == '__main__':
    root = ListNode(val=2)
    root.next = ListNode(val=1)
    root.next.next = ListNode(val=4)
    root.next.next.next = ListNode(val=3)
    root.next.next.next.next = ListNode(val=5)
    res = Solution().nextLargerNodes(root)
    print(res)