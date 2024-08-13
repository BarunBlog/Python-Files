
class Node:

    def __init__(self, val: int) -> None:
        self.data = val
        self.left = None
        self.right = None


def preOrder(root: Node):
    if root == None:
        return
    
    print(root.data, end=" ")

    preOrder(root.left)
    preOrder(root.right)


def inOrder(root: Node):
    if root == None:
        return

    inOrder(root.left)

    print(root.data, end=" ")

    inOrder(root.right)


def postOrder(root: Node):
    if root == None:
        return

    postOrder(root.left)
    
    postOrder(root.right)
    
    print(root.data, end=" ")



def main():
    """
            1
          /   \
         2     3
       /   \ /   \
      4    5 6    7

    """

    # Generating tree
    root = Node(val=1)

    root.left = Node(2) 
    root.right = Node(3) 

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    preOrder(root)
    print()

    inOrder(root)
    print()

    postOrder(root)
    print()


if __name__ == "__main__":
    main()