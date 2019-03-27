import math
import sys

class Node:

    def __init__(self, val = None):
        self.val = val
        self.next = None

    def printList(self):
        head = self
        while(head.next):
            print(head.next.val)
            head = head.next

def reverseList(head):

    if not head.next:
        return head

    mid = head.next
    back = head
    newEnd = mid

    while mid:
        front = mid.next
        mid.next = back
        back = mid
        mid = front

    newEnd.next = None
    newHead = Node()
    newHead.next = back

    return newHead

def mergeLists(head1, head2):

    curr1, curr2 = head2, head2

    if curr1.val > curr2.val:
        newHead = curr1
    else:
        newHead = curr2

    newIterator = newHead

    while curr1 and curr2:
        if curr1.next.val > curr2.val:
            newIterator.next = curr1.next
            curr1 = curr1.next
        else:
            next = curr1.next
            newIterator.next = curr2
            curr2 = curr2.next
            curr1 = next

    return newIterator

def main():

    head = Node()

    iter = head
    for i in range(10):
        iter.next = Node(i)
        iter = iter.next

    fiveList = Node()
    iter = fiveList
    for i in range(51):
        if i % 5 == 0:
            iter.next = Node(i)
            iter = iter.next

    squareList = Node()
    iter = squareList
    for i in range(101):
        root = math.pow(i, .5)
        if math.ceil(root) == root:
            iter.next = Node(i)
            iter = iter.next

    head = reverseList(head)
    head.printList()

    #merged = mergeLists(fiveList, squareList)
    #merged.printList()

    print(sys.version)

main()

