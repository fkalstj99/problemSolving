class CircularQueue():
  def __init__(self, size):
    self.queue = [0 for x in range(size+1)]
    self.front = 0
    self.rear = 0
    self.max_size = size
    self.list_size = size + 1
    

  
  def enQueue(self, num):
    if(self.rear + 1) % self.list_size == self.front:
      return -1
  
    self.queue[self.rear] = num
    self.rear = (self.rear + 1) % self.list_size
    
    
  def size(self):
    if self.front == self.rear:
      return 0
    elif self.rear > self.front:
      return self.rear - self.front
    else:
      return self.max_size - (self.front - self.rear) + 1  
  

  def dequeue(self):
    if self.size() == 0:
      return - 1
    temp = self.queue[self.front]
    self.front = (self.front +  1) % self.list_size
    return temp

  def empty(self):
    return 1 if self.front == self.rear else 0





n , k = map(int, input().split())

queue = CircularQueue(n)

output = ""

for i in range(1, n+1):
  queue.enQueue(i)
  
while(True):
  for i in range(k-1):
    queue.enQueue(queue.dequeue())
  output = output + str(queue.dequeue())
  
  if queue.empty() == 1:
    break
  else:
    output = output + ", "
  

print("<"+output+">")


#list가 0이 될때까지 끊임없이 순환한다.
#7 3                         output(요세푸스)
# 1 2 3 4 5 6 7 |           |
# 1 2 3 4 5 6 7 | 1         |
# 1 2 3 4 5 6 7 | 1 2       |
# 1 2 3 4 5 6 7 | 1 2       |   3
# 1 2 3 4 5 6 7 | 1 2 4     |   3
# 1 2 3 4 5 6 7 | 1 2 4 5   |   3
# 1 2 3 4 5 6 7 | 1 2 4 5   |  3, 6
# 1 2 3 4 5 6 7 | 1 2 4 5 7 |  3, 6
#     o     o       o     o  