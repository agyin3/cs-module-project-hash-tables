class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value, prev_node=None, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev

    def set_next(self, next_node=None):
        self.next = next_node

    def set_value(self, val):
        self.value = val
    
    def set_prev(self, prev_node=None):
        self.prev = prev_node



class HashLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0 if self.head is None else 1

    def get_length(self):
        return self.length

    def add_to_tail(self, key, value):
        new_node = HashTableEntry(key, value, prev_node=self.tail)

        if self.head is None:
            self.head = new_node
        
        else:
            self.tail.set_next(new_node)

        self.tail = new_node
        self.length += 1

    def remove_from_tail(self):
        if self.tail is None and self.head is None:
            return None

        value = self.tail.get_value()

        if self.tail is self.head:
            self.tail = None
            self.head = None
        
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next()

        self.length -= 1
        return value

    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None

        value = self.head.get_value()
        
        if self.head is self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.head = self.head.get_next()
            self.head.set_prev()
        
        self.length -= 1
        return value

    def contains(self, key):
        if self.head is None:
            return None
        
        curr_node = self.head

        while curr_node.get_key() != key:
            if curr_node.get_next() is None:
                return None
            
            curr_node = curr_node.get_next()

        return curr_node

    
    def delete(self, node):
        if self.tail is None and self.head is None:
            return None

        elif self.tail is self.head:
            self.head = None
            self.tail = None
            self.length -= 1

        elif node is self.head:
            self.remove_from_head()
        
        elif node is self.tail:
            self.remove_from_tail()

        else:
            curr_node = self.head
            prev_node = None
            next_node = self.head.get_next()

            while curr_node is not node:
                prev_node = curr_node
                curr_node = next_node
                next_node = curr_node.get_next()
            
            prev_node.set_next(next_node)
            next_node.set_prev(prev_node)
            curr_node = None
            self.length -= 1
            


