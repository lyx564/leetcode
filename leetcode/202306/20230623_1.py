"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # 哈希表，空间复杂度O(n)
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None

        node_pos = {head: 0}
        c_head = Node(head.val, None, None)
        o_head, o_c_head = head, c_head
        head = head.next
        pos = 1
        c_pos_node = {0: c_head}
        while head:
            node_pos[head] = pos
            c_head.next = Node(head.val, None, None)
            c_head = c_head.next
            c_pos_node[pos] = c_head
            pos += 1
            head = head.next
        res_node = o_c_head
        while o_head:
            assert o_head.val == o_c_head.val
            if not o_head.random:
                o_c_head.random = None
            else:
                o_c_head.random = c_pos_node[node_pos[o_head.random]]
            o_head = o_head.next
            o_c_head = o_c_head.next
        return res_node

    # 迭代，空间复杂度O(1)
    def copyRandomList_1(self, head: Node) -> Node:
        if not head:
            return None
        o_head = head
        while head:
            node = Node(head.val, None, None)
            node.next = head.next
            head.next = node
            head = node.next
        head = o_head
        while head:
            if not head.random:
                head.next.random = None
            else:
                head.next.random = head.random.next
            head = head.next.next

        res_node, c_head = o_head.next, o_head.next
        while c_head.next:
            c_head.next = c_head.next.next
            c_head = c_head.next

        return res_node


if __name__ == '__main__':
    head = Node(7, None)
    head.next = Node(13, None)
    head.next.next = Node(11, None)
    head.next.next.next = Node(10, None)
    head.next.next.next.next = Node(1, None)
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head

    res = Solution().copyRandomList_1(head)
    print(res)
