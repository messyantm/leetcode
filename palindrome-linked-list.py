"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
"""
from util import ListNode


# 0 1 2
# 0 1 2 3

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        quick = head.next
        slow_pre = None
        slow_cur = head
        while quick and quick.next:
            quick = quick.next.next
            tmp = slow_cur.next
            slow_cur.next = slow_pre
            slow_pre = slow_cur
            slow_cur = tmp
        if quick:
            go_node = slow_cur.next
            slow_cur.next = slow_pre
            back_node = slow_cur
        else:
            go_node = slow_cur.next
            back_node = slow_pre
        # if go_node is None:  # 0
        #     return True
        # if back_node is None and back_node.val == go_node.val:
        #     return True  # 0 1
        while go_node and back_node:
            if go_node.val != back_node.val: return False
            go_node = go_node.next
            back_node = back_node.next
        return True

    class Solution(object):
        def isPalindrome(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            # 反转链表，快慢指针,找到链表的中心位置，一个指针跟在慢指针后反转链表
            RHead = None
            if not head or not head.next:
                return True
            else:
                slow = head
                quick = head.next

            while quick and quick.next:
                temp = slow
                slow = slow.next
                quick = quick.next.next
                temp.next = RHead
                RHead = temp


            if quick:  # 偶数
                quick = slow.next
                slow.next = RHead
            else:
                quick = slow.next
                slow = RHead

            while quick and slow:
                if quick.val != slow.val:
                    return False
                else:
                    quick = quick.next
                    slow = slow.next
            return True
