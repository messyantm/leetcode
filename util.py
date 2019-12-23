class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def show_linked_list(head):
    cur = head
    value_list = []
    while cur:
        value_list.append(cur.val)
        cur = cur.next
    print(value_list)


def create_linked_list(num):
    node_values = range(2, num)
    root = ListNode(1)
    lasted = root
    for i in node_values:
        cur = ListNode(i)
        lasted.next = cur
        lasted = cur
    return root
