from dataclasses import dataclass

@dataclass
class Node:
    data: any
    def __post_init__(self) -> None:
        self.next = None
        
class LinkedList:
    """If the head of a linkedlist is null, the list is empty.
    The linkedlist ends when the next pointer is null"""
    def __init__(self, head: Node) -> None:
        self.head = head

    def __repr__(self) -> str:
        """This is not very efficient because it uses space
        and time complexity of O(n)"""
        llist = []
        if not self.head:
            llist.__repr__()  

        current = self.head
        llist.append(current)
        while current.next:
            llist.append(current.next)
            current = current.next
        
        return llist.__repr__()    

    def append(self, data) -> None: 
        """Time complexity is O(n)"""
        if not self.head:
            self.head = Node(data)
            return
        current = self.head    
        while current.next:
            current = current.next
        current.next = Node(data)    

    def prepend(self, data) -> None:
        """Time complexity is O(1)"""
        if not self.head:
            self.head = Node(data)
            return     
        current = self.head
        newHead = Node(data)
        newHead.next = current    
        self.head = newHead

    def delete(self, data) -> None:
        """Time complexity is O(n) while 
        deleting the first element is O(1)"""
        if not self.head:
            return  

        current = self.head
        if current.data == data:
            self.head = current.next
            return

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next    

    def insert(self, data, position: int) -> None: 
        """Time complexity is O(n)"""
        if not self.head:
            self.head = Node(data)
            return  

        current = self.head
        idx = 0
        if idx == position:
            newHead = Node(data)
            newHead.next = current    
            self.head = newHead
            return

        while current.next:
            if (idx+1) == position:
                tmp = current.next
                current.next = Node(data)
                current.next.next = tmp
                break
            idx += 1
            current = current.next    
    
    def has_cycle(head: Node) -> int:
        visited = []
        current = head
        while current.next:
            if current in visited:
                return 1
            visited.append(current)
            current = current.next
        return 0    

if __name__ == '__main__':
    head = Node(2)
    llist = LinkedList(head)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    llist.append(6)
    llist.prepend(1)
    llist.delete(5)
    llist.insert(7,2)
    print(llist)            