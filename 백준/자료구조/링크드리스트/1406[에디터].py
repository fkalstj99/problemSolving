import sys



class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None
   

class DLinkedList:
  def __init__(self, str):
    self.head = Node(0)
    begin = self.head
    for s in str:
      t = Node(s)
      t.prev = begin
      begin.next = t
      begin = t
    self.cursor = begin

  def L(self):
    if self.cursor.prev:
      self.cursor = self.cursor.prev
  
  def D(self):
    if self.cursor.next:
      self.cursor = self.cursor.next

  def B(self):
    prev = self.cursor.prev
    next = self.cursor.next
    if prev:
      prev.next = next
      if next:
        next.prev = prev 
      self.cursor = prev
  
  def P(self, item):
    t = Node(item)
    prev = self.cursor
    next = self.cursor.next
    self.cursor = t
    if prev:
      prev.next = self.cursor
    if next:
      next.prev = self.cursor
    self.cursor.prev = prev
    self.cursor.next = next
  
  def print(self):
    self.cursor=self.head.next
    while self.cursor:
      print(self.cursor.data)
      self.cursor=self.cursor.next  






str = sys.stdin.readline().rstrip()
print=sys.stdout.write
DLList = DLinkedList(str())
for i in range(int(input())):
  input_split = sys.stdin.readline().split()
  operator = input_split[0]

  if operator=="L":
    DLList.L()
  elif operator =="D":
    DLList.D()
  elif operator == "B":
    DLList.B()
  else:
    DLList.P(input_split[1])

DLList.print()