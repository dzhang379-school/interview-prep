# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def addTwoNumbers1(self, l1, l2):

        head = retNode = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            head.val = sum % 10
            carry = sum // 10

            if l1 or l2 or carry:
                head.next = ListNode(0)
                head = head.next

        return retNode