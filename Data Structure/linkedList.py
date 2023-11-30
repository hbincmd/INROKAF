class Node:
    def __init__(self, value):
        self.value = value
        self.link = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def show(self):
        top = self.head
        llarray = []
        llarray.append(top.value)
        while top.link is not None:
            top = top.link
            llarray.append(top.value)
        
        print('->'.join(map(str, llarray)) + "->None")
        
    def add(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            top = self.head
            while top.link is not None:
                top = top.link
            
            top.link = Node(value)
            
    def remove(self, value):
        top = self.head
        while top.link.value is not value:
            top = top.link
        
        top.link = top.link.link

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.show()

ll.remove(2)
ll.show()