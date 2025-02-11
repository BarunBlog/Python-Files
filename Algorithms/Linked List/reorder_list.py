# Leetcode: reorderList

class ListNode:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None


class Solution:

    def reorderList(self, head: list[ListNode]) -> None:
        stack: list[ListNode] = []
        current = head

        while current:
            stack.append(current)

            current = current.next

        current = head

        while current != stack[-1]:
            node = stack.pop()

            temp = current
            current = current.next

            temp.next = node

            if node == current:
                break

            node.next = current
        

        current.next = None


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
    arr1 = [1,2,3,4,5,6,7,8]

    for item in arr1:
        head1 = ob.insert_at_tail(head1, item)
    
    ob.reorderList(head1)

    ob.display(head1)
    


if __name__ == "__main__":
    main()