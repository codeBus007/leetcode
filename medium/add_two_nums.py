# coding: utf-8

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
# 单向链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    思路:
        carray 进位 初始为0
        p,q carray 值相加 (若有任意点为None p/q 置为0) 和大于等于10 carray置为 1 否则置为0
        迭代至下一个节点
       *若迭代至最后一点需要进位
    """
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        carray = 0
        head = None
        while l1 is not None or l2 is not None:
            p = l1.val if l1 is not None else 0
            q = l2.val if l2 is not None else 0

            value = p + q + carray
            if value >= 10:
                carray = 1
                value = value - 10
            else:
                carray = 0

            node = ListNode(value)

            if head is None:
                head = node
                
            else:
                cur.next = node

            cur = node
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # 迭代完 判断最后一位是否需要进位
        if carray == 1:
            cur.next = ListNode(1)

        return head

def travel(l:ListNode):
    cur = l
    while l is not None:
        print(l.val)
        l = l.next


if __name__ == '__main__':
    head1 = ListNode(1)
    head2 = ListNode(9)
    head2.next = ListNode(9)

    s = Solution()
    head = s.addTwoNumbers(head1, head2)

    travel(head)







