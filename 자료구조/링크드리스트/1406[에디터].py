import sys



class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None
   





class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
 
    def Insert(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.tail.prev = newNode
            newNode.next = self.tail
            newNode.prev = self.tail.prev.prev

    def moveRight(self):
        if self.tail == None:
            return
        
        self.tail = self.tail.next

    def moveLeft(self):
        if self.tail.prev == self.head:
            return
        
        self.tail = self.tail.prev

    def Delete(self):
        if self.tail.prev == self.head:
            return
        
        self.tail.prev = self.tail.prev.prev
        self.tail.next = self.tail.prev.next
        del self.tail.prev
    
    def Print(self):
      temp = self.head
      while temp.next != None:
        print(temp.data)
        temp = temp.next  

str = sys.stdin.readline()
num = int(sys.stdin.readline())

DLList = DLinkedList(str)


for i in range(num):
  input_split = sys.stdin.readline().split()
  operator = input_split[0]

  if operator=="L":
    DLList.moveLeft()
  elif operator =="D":
    DLList.moveRight()
  elif operator == "B":
    DLList.Delete()
  else:
    DLList.Insert(input_split[1])


#tail을 커서의 역할로 사용