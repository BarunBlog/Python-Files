
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:

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

    def reverseList(self, head: list[ListNode]) -> list[ListNode]:
        if head == None:
            return head

        prev = None
        current = head

        while current != None:
            temp = current
            current = current.next

            temp.next = prev
            prev = temp
        
        return prev


def main():
    ob = Solution()
    head: ListNode = None
    arr = [0,1,2,3]

    for item in arr:
        head = ob.insert_at_tail(head, item)

    # ob.display(head)

    head = ob.reverseList(head)

    ob.display(head)

if __name__ == "__main__":
    main()