# Leetcode: 2. Add two numers

from typing import Optional

class ListNode:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2

        counter = 1
        num1 = 0
        while current1:
            num1 += current1.val * counter

            counter *= 10
            current1 = current1.next

        counter = 1
        num2 = 0
        while current2:
            num2 += current2.val * counter

            counter *= 10
            current2 = current2.next

        result = num1 + num2

        if result == 0:
            return ListNode(0)

        dummyNode = ListNode(-1)
        prev = None
        

        while result != 0:
            digit = result % 10
            node = ListNode(digit)

            if prev:
                prev.next = node
            else:
                dummyNode.next = node

            result //= 10
            prev = node


        return dummyNode.next



    def insert_at_tail(self, head: ListNode, val: int) -> ListNode:
        current = head
        new_node = ListNode(val)

        if not head:
            head = new_node
            return head

        while current.next:
            current = current.next

        current.next = new_node

        return head

    
    
    def display(self, head: ListNode):
        current = head

        while current:
            print(current.val)
            current = current.next


def main():
    ob = Solution()
    head1: ListNode = None
    head2: ListNode = None

    arr1 = [0]
    arr2 = [0]

    for item in arr1:
        head1 = ob.insert_at_tail(head1, item)

    for item in arr2:
        head2 = ob.insert_at_tail(head2, item)
    
    head3: ListNode = ob.addTwoNumbers(head1, head2)

    ob.display(head3)
    


if __name__ == "__main__":
    main()