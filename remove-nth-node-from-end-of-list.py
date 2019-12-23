"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_list = list()
        cur = head
        while cur:
            node_list.append(cur)
            cur = cur.next
        target_node = node_list[-n]
        last_node = node_list[-n - 1]
        if last_node == head:  # -n始终有效，当删除节点为第一个时候，直接返回
            return head.next
        last_node.next = target_node.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        """双指针解法
        初始情况:
        第一个指针为0位置的指针
        第二个指针为n+1位置的指针
        第一个指针的下一个就为要删除的指针
        第一个指针为None时
        """
        first = head
        second = head
        for i in range(n + 1):
            if second is None:  # 特殊: 当n为整个链表的长度时前进n步，fisrt为None, 直接返回head的下一个值
                return head.next
            second = second.next
        while second:
            second = second.next
            first = first.next
        first.next = first.next.next
        return head
