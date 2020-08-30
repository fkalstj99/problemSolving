class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class Deque:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0
  
  def empty(self):
    if not self.front:
      return True
    return False
  
  def push_front (self, data):
    newNode = Node(data)
    if self.empty():
      self.front = newNode
      self.rear = newNode
    else:
      self.front.prev = newNode
      self.front = newNode
    self.size += 1


  def push_back (self, data):
    newNode = Node(data)
    if self.empty():
      self.front = newNode
      self.rear = newNode
    else:
      self.rear.next = newNode
      self.rear = newNode
    self.size += 1


  def pop_front(self):
    if self.empty():
      return -1
    temp = self.front
    if(self.front == self.rear):
      self.rear = -1

    
    self.front = self.front.next
    self.size-=1
    return temp.data

  def pop_back(self):
    if self.empty():
      return -1

    temp = self.rear
    if(self.front == self.rear):
      self.rear = -1
    

    self.rear = self.rear.prev
    self.size-=1
    return temp.data


  def front(self):
    if self.front == None:
      return -1
    return self.front.data
  

  def back(self):
    if self.rear == None:
      return -1
    return self.rear.data

  def size(self):
    return self.size
    





import collections

class water:
    def __init__(self):
        self.deque = collections.deque()

    def push_back(self, num):
        self.deque.append(num)
    
    def push_front(self, num):
        self.deque.appendleft(num)
    
    def pop_front(self):
        if self.deque:
            return self.deque.popleft()
        else:
            return -1
        
    def pop_back(self):
        if self.deque:
            return self.deque.pop()
        else:
            return -1

    def size(self):
        return len(self.deque)

    def empty(self):
        if self.deque:
            return 0
        else:
            return 1
        
    def front(self):
        if self.deque:
            return self.deque[0]
        else:
            return -1
    
    def back(self):
        if self.deque:
            return self.deque[-1]
        else:
            return -1
        

test = int(input())
case = water()
result = []
for i in range(test):
    a = input()
    if " " in a:
        a, b = a.split()
        
    if a == "push_back":
        case.push_back(b)
    elif a == "push_front":
        case.push_front(b)
    elif a =="pop_front":
        result.append(case.pop_front())
    elif a =="pop_back":
        result.append(case.pop_back())        
    elif a =="size":
        result.append(case.size())
    elif a =="empty":
        result.append(case.empty())
    elif a =="front":
        result.append(case.front())
    elif a =="back":
        result.append(case.back())

for i in result:
    print(i)