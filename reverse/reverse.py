class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #last one should point to none
        if node is None:
            return None
        #base to meet condition before calling recursion again
        if node.next_node is not None:
            #var to store next node before changing to prev
            new_node = node.next_node
            node.next_node = prev
            #send new_node as an argument for node and node for prev
            return self.reverse_list(new_node, node)
        else:
            #swap the head for the input node and the previous
            self.head = node 
            node.next_node = prev




# ll = LinkedList()
# ll.add_to_head(1)
# ll.add_to_head(2)
# ll.add_to_head(10)
# print(ll.head.value)
# print(ll.head.next_node.value)
# print(ll.contains(2))
# print(ll.reverse_list(ll.head, None))
# print(ll.head.value)
# print(ll.head.next_node.value)
