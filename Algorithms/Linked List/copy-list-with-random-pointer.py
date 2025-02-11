# Leetcode: 138. Copy list with random pointer

from typing import Dict, Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None) -> None:
        self.val = int(x)
        self.next = next
        self.random = random
    


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head == None:
            return None
        
        hashMap: Dict[Node, Node] = {}

        current = head
        while current:
            node = Node(current.val)
            hashMap[current] = node

            current = current.next

        current = head
        while current:
            currentNode = hashMap[current]
            currentNode.next = None if current.next == None else hashMap[current.next]
            currentNode.random = None if current.random == None else hashMap[current.random]

            current = current.next
        
        return hashMap[head]


    def createRandomList(self, li: list[list[int]]) -> Node:
        nodes: list[Node] = []
        prev: Node = None

        prev = Node(x=li[0][0])
        nodes.append(prev)

        for pair in li[1:]:
            currentNode = Node(x=pair[0])
            prev.next = currentNode

            nodes.append(currentNode)
            prev = currentNode
            
        currentNode.next = None

        i = 0
        for pair in li:
            if pair[1] != None:
                randomNode = nodes[pair[1]]
            else:
                randomNode = None
            
            node = nodes[i]
            node.random = randomNode
            
            i += 1

        
        return nodes[0]
    
    
    def display(self, head: Node):
        current = head

        while current:
            print(current.val, current.next, current.random)
            current = current.next


def main():
    li = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    ob = Solution()

    head: Node = ob.createRandomList(li)
    ob.display(head)

    print("List after cloning")
    copiedListHead = ob.copyRandomList(head)
    ob.display(copiedListHead)


if __name__ == "__main__":
    main()


        

        
            
        
        
        


        

        


