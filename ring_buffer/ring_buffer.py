class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
        self.old_node = self.head

    def add_to_tail(self, value):
        new_node = Node(value)
        self.length += 1
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.old_node = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    def remove_from_head(self):
        if self.head is None:
            return None
        elif self.head.next is not None:
            prev_head = self.head
            self.head = prev_head.next
            prev_head.next = None
        self.length -= 1

    # def add_to_head(self, value):
    #     new_node = Node(value)
    #     self.length += 1
    #     #change head to point to new node
    #     if self.head is None and self.tail is None:
    #         self.head = new_node
    #         self.tail = new_node
    #         self.old_node = new_node
    #         return
    #     else:
    #         #change head to point to next
    #         old_head = self.head
    #         self.head = new_node
    #         self.head.next = old_head

    # def remove_from_tail(self):
    #     #access tail value
    #     if self.head is None and self.tail is None:
    #         return
    #     self.length -= 1
    #     if self.head.next is None and self.head is not None:
            
    #         value = self.head #save value of head
    #         self.head = None
    #         self.tail = None
    #         return value
    #     n = self.head
    #     value = self.tail
    #     while n.next is not None:
    #         n = n.next

    #     self.tail = n.prev
    #     n.prev = None
    #     self.tail.next = None
    #     n = None
    #     return value


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()

    def append(self, item):
        #check capacity size, if full pop last one and replace with new one
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else:
            #add item to old node
            self.storage.old_node.value = item

            #check if old node next is none
            if self.storage.old_node.next is not None:
                self.storage.old_node = self.storage.old_node.next
            # replace old node with new item
            else: 
                self.storage.old_node = self.storage.head

    def get(self):
        #return all the elements in the stack
        buffer_list = []
        if self.storage.head:
            node = self.storage.head
            while node:
                buffer_list.append(node.value)
                node = node.next
            return buffer_list

rbuffer = RingBuffer(3)
rbuffer.append("a")
rbuffer.append("b")
rbuffer.append("c")
print(rbuffer.get())
rbuffer.append("d")
print(rbuffer.get())