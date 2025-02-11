# Leetcode: Remove Node From End of Linked List

class ListNode:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None


class Solution:

    def removeNthFromEnd(self, head: list[ListNode], n: int) -> list[ListNode]:
        ln = 0
        current = head

        while current:
            current = current.next
            ln += 1
        
        if ln == 1:
            return None
        
        current = head
        dummyNode = ListNode(-1)
        prev = dummyNode

        prev.next = current

        position = 1

        while current:
            if position == ln - n + 1:
                prev.next = current.next
            
            position += 1
            current = current.next
            prev = prev.next

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
    # arr1 = [1,2,3,4,5,6,7,8,9]
    arr1 = [1,2,3,4]
    n = 2

    for item in arr1:
        head1 = ob.insert_at_tail(head1, item)
    
    head1 = ob.removeNthFromEnd(head1, n)

    ob.display(head1)
    


if __name__ == "__main__":
    main()