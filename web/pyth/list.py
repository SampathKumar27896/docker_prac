class node:
    def __init__(self,data):
        self.data = data
        self.next = next 

class linkedList:
    def __init__(self):
        self.head = None 

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
if __name__ == '__main__':

    llist = linkedList()
    llist.head = node(1)
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third

