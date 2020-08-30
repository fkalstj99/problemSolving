
import sys


#list 이용구현
class Stack:
    def __init__(self):
        self.len = 0
        self.list = []
        
    def push(self, num):
        self.list.append(num)
        self.len += 1
    
    def pop(self):
        if self.size() == 0:
            return -1
        pop_result = self.list[self.len - 1]
        del self.list[self.len - 1]
        self.len -= 1
        return pop_result
        
    def size(self):
        return self.len
        
    def empty(self):
        return 1 if self.len == 0 else 0
        
    def top(self):
        return self.list[-1] if self.size() != 0 else -1
        
 
num = int(sys.stdin.readline())
stack = Stack()
for i in range(num):
    input_split = sys.stdin.readline().split()
    op = input_split[0]
 
    if op == "push":
        stack.push(input_split[1])
    elif op == "pop":
        print(stack.pop())
    elif op == "size":
        print(stack.size())
    elif op == "empty":
        print(stack.empty())
    elif op == "top":
        print(stack.top())
    else:
        print("unacceptable op")






#노드 이용 구현
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
  
  def is_empty(self):
    if not self.top:
      return True
    
    return False
  
  def push(self, data):
    new_node = Node(data)

    new_node.next = self.top
    self.top = new_node
    self.size += 1

  def pop(self):
    if self.is_empty():
      return -1

    data = self.top.data
    self.top = self.top.next
    self.size -= 1
    return data

  def top(self):
    if self.top == None:
      return -1
    return self.top.data
  
  def size(self):
    return self.size
    

