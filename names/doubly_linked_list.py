class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # increase the length
        self.length += 1
        new_node = ListNode(value)
        # an empty list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if head and tail are none
        if self.head is None and self.tail is None:
            return None

        self.length -= 1

        # if there is only one node in the list
        if self.head == self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.value
            self.head = self.head.next
            return val

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # increase the length
        self.length += 1
        new_node = ListNode(value)
        # an empty list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if head and tail are none
        if self.head is None and self.tail is None:
            return None

        self.length -= 1

        # if there is only one node in the list
        if self.head == self.tail:
            val = self.tail.value
            self.head = None
            self.tail = None
            return val
        else:
            val = self.tail.value
            self.tail = self.tail.prev
            return val

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if the node moving is the head
        if node == self.head:
            return
        elif node == self.tail:
            # resetting the tail
            self.tail = node.prev
            self.tail.next = None
        else:
            # get the prev/next for the node to move
            # set them to each others prev/next
            node.prev.next = node.next
            node.next.prev = node.prev

        # move to the head
        self.head.prev = node
        node.next = self.head
        self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if the node moving is the head
        if node == self.tail:
            return
        elif node == self.head:
            # resetting the head
            self.head = node.next
            self.head.prev = None
        else:
            # get the prev/next for the node to move
            # set them to each others prev/next
            node.prev.next = node.next
            node.next.prev = node.prev

        # move to the tail
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        else:
            if node == self.head:
                self.head = node.next
            elif node == self.tail:
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # start at the head for node/value
        current_node = self.head
        max_value = self.head.value

        # go through all the nodes till the tail checking the values
        while current_node != self.tail:
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value

        return max_value

    def contains(self, value):
        # check if the list is empty
        if self.head is None and self.tail is None:
            return False

        current_node = self.head
        while current_node != None:
            if current_node.value == value:
                self.delete(current_node)
                return True
            else:
                current_node = current_node.next

        return False