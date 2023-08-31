class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummy = Node(0)
        self.head = self.dummy.next

    def get(self, index: int) -> int:
        i = -1
        ptr = self.dummy
        while ptr != None and i != index:
            ptr = ptr.next
            i+=1

        if ptr is None:
            return -1
        return ptr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node 
        

    def addAtTail(self, val: int) -> None:
        # Adds a new node at the "end"
        new_node = Node(val)
        ptr = self.dummy
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None: 
        new_node = Node(val)
        ptr = self.dummy
        i = 0
        while ptr != None and i != index:
            ptr = ptr.next
            i += 1 
        
        if ptr:
            new_node.next = ptr.next
            ptr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        ptr = self.dummy
        while ptr != None and i != index:
            ptr = ptr.next
            i+=1
        if ptr and ptr.next:
            ptr.next = ptr.next.next

    # def printLinkedList(self):
    #     ptr = self.head.next
    #     ans = ''
    #     while ptr != None:
    #         ans += f"{ptr.val}" + "->" if ptr.next else ""
    #         ptr = ptr.next 
    #     return ans 

# obj = MyLinkedList() 
# obj.printLinkedList()
# for i in range(10**3):
#     obj.addAtTail(obj) 
# obj.deleteAtIndex(10) 
# ans = obj.printLinkedList() 
# print(ans[-10:])



# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)