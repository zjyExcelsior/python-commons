# coding=utf-8
"""反转链表：输入链表的头结点，输出反转后链表的头结点"""


class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return '<Node value=%s>' % self.value


def reverse_link_list(head=None):
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    while cur:
        new_head = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return new_head


if __name__ == '__main__':
    print reverse_link_list()
    print reverse_link_list(None)
    head = Node(1)
    print reverse_link_list(head)
    p1 = Node(2)
    p2 = Node(3)
    p3 = Node(4)
    head.next = p1
    p1.next = p2
    p2.next = p3

    new_head = reverse_link_list(head)
    print new_head
