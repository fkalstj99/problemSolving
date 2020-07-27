import sys


class Queue:
  def __init__(self):
    self.len = 0
    self.list = []

  def push(self, num):
    self.list.append(num)
    self.len += 1
  
  def pop(self):
    if self.empty():
      return -1
    self.len -= 1
    return self.list.pop(0)
    

  def size(self):
    return self.len
  

  def empty(self):
    if self.len == 0:
      return 1
    return 0

  def front(self):
    if self.empty():
      return -1
    return self.list[0]


  def back(self):
    if self.empty():
      return -1
    return self.list[len(self.list)-1]


num = int(sys.stdin.readline())
queue = Queue()
for i in range(num):
    input_split = sys.stdin.readline().split()
    op = input_split[0]
 
    if op == "push":
        queue.push(input_split[1])
    elif op == "pop":
        print(queue.pop())
    elif op == "size":
        print(queue.size())
    elif op == "empty":
        print(queue.empty())
    elif op == "front":
        print(queue.front())
    else:
        print(queue.back())




#링크드리스트
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0
  
  def empty(self):
    if not self.front:
      return True
    return False
  
  def push(self, data):
    newNode = Node(data)
    if self.empty():
      self.front = newNode
      self.rear = newNode
    else:
      self.rear.next = newNode
      self.rear = newNode


  def pop(self):
    if self.empty():
      return -1

    temp = self.front
    if(self.front == self.rear):
      self.rear = -1
    
    self.first = self.first.next
    self.size-=1
    return temp.data

  def top(self):
    if self.front == None:
      return -1
    return self.front.data
  
  def size(self):
    return self.size
    