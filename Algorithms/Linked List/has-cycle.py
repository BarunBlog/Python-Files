
class ListNode:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None


class Solution:
    def hasCycle(self, head: list[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head.next

        while fast.next != None:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next

        return False
    

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
    

    def create_cycle(self, head: ListNode, pos: int) -> None:
        if pos == -1:
            return
         
        current = head
        i = 0
        node: ListNode = None

        # Special case: Single node with a cycle (pos == 0)
        if current and not current.next:
            if pos == 0:
                current.next = current  # Single node cycle
            return

        while current.next:
            if i == pos:
                node = current
            
            current = current.next
            i += 1
        
        current.next = node
        

    
    
    def display(self, head: ListNode):
        current = head

        while current:
            print(current.val)
            current = current.next


def main():
    ob = Solution()
    head1: ListNode = None
    arr1 = [3]
    pos = 0

    for item in arr1:
        head1 = ob.insert_at_tail(head1, item)

    ob.create_cycle(head1, pos)
    
    print(ob.hasCycle(head1))




if __name__ == "__main__":
    main()