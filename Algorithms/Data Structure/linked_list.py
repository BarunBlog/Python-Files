
class Node:

    def __init__(self, val):
        # setting instance variable
        self.data: int = val
        self.next: Node = None


def insert_at_tail(head: Node, val: int) -> Node:
    current = head
    new_node = Node(val)

    if not head:
        head = new_node
        return head

    while current.next:
        current = current.next

    current.next = new_node

    return head


# remove all elements that match the given value
def remove_elements(head: Node, val: int) -> Node:
    if not head:
        return head

    dummy_node = Node(-1)
    current = head
    prev = dummy_node
    prev.next = current

    while current.next:
        if current.data == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return dummy_node.next


def display(head: Node):
    current = head

    while current:
        print(current.data)
        current = current.next


def main():
    head: Node = None
    arr = [1, 2, 4, 1, 3, 5]

    for item in arr:
        head = insert_at_tail(head, item)

    head = remove_elements(head, 1)

    display(head)


if __name__ == "__main__":
    main()
    
