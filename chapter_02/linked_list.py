from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return f"Node({self.value})"
    
class SingleLinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.size = 0
        
        if values is not None:
            self.add_multiple(values)
            
    def __iter__(self):
        curr = self.head
        
        while curr:
            yield curr 
            curr = curr.next 
        
    def __str__(self):
        values = [str(x) for x in self]
        return f" -> ".join(values)
    
    def __len__(self):
        return self.size
        # result = 0
        # curr = self.head
        
        # while curr:
        #     result += 1
        #     curr = curr.next 
            
        # return result
    
    def add(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
            
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        
        self.size += 1
        return self.tail
    
    def add_multiple(self, values):
        for v in values:
            self.add(v)
            
    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        
        for _ in range(n):
            self.add(randint(min_value, max_value))
            
        return self