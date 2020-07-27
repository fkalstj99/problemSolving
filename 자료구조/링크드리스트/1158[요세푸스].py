class Node:
  def __init__(self, item):
    self.data = item
    self.next = None



class CircularLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None


  def Insert(self, item):
    newNode = Node(item)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      newNode = self.tail 

  def remove(self):
    