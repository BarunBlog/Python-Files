
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:

        cur1 = list1
        cur2 = list2
        dummyNode = ListNode(-1)
        result = dummyNode

        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                result.next = cur1
                cur1 = cur1.next
            else:
                result.next = cur2
                cur2 = cur2.next
            
            result = result.next

        if cur1:
            result.next = cur1
        if cur2:
            result.next = cur2
        
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


def  main():
    ob = Solution()
    head1: ListNode = None
    head2: ListNode = None
    arr1 = [1,2,4]
    arr2 = [1,3,5]

    for item in arr1:
        head1 = ob.insert_at_tail(head1, item)

    for item in arr2:
        head2 = ob.insert_at_tail(head2, item)

    head3 = ob.mergeTwoLists(list1=head1, list2=head2)

    ob.display(head3)

if __name__ == "__main__":
    main()