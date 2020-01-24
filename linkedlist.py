class Item:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,val):
        # Adds an item to front (head) of the linkedlist
        newItem = Item(val) # Creates a new BOX
        newItem.next = self.head # Points Box to curr head
        self.head = newItem  # Makes box new head 

    def display(self):
        curr = self.head
        while curr != None: 
            print(str(curr.val)+"->",end = '')
            curr = curr.next 
        print("None")
    
    # Reverses a linked list
    def reverse(self):
        if self.head is not None:
            self.reverseActual(self.head)
    def reverseActual(self, curr):
        if curr.next is None:
            self.head = curr
            return
        self.reverseActual(curr.next)
        curr.next.next = curr
        curr.next = None
        
        

# Create an object of class linkedlist
ll1  = Linkedlist()
ll1.insertAtBegin(1)
ll1.insertAtBegin(2)
ll1.insertAtBegin(3)
ll1.display()
ll1.reverse()
ll1.display()