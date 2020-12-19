class Node(object):
  def __init__(self,value):
    self.value = value
    self.next = None

class Queue(object):
  
  j = 0


  def __init__(self,size):
    self.array = [0 for i in range(size)]
    self.head = None
    self.tail = None
    self.size = size

  def isempty(self):
    x = self.tail
    y = self.head
    empty = True if (x and y ) is None else False
    return empty

  def Enqueue(self,value):
    n = Node(value)
    x = self.tail
    y = self.head

    if self.isempty() :
      self.head = n
      self.tail = n
    elif self.isfull():

      print('Queue Overflow')
    else:
      x.next = n
      self.tail = n
      x = None
      self.j+=1
  def Dequeue(self):
    x = self.head
    if x == None:
      print('Queue underflow')
    elif x.next == None:
      self.head = None
      x = None
    else:
      self.head = x.next
      x = None
      self.j-=1



  def isfull(self):
    full = True if self.j >= self.size else False
    return full


  def Print(self):
    x = self.head
    
    while x:
      print(x.value,end=' <-- ')
      x=x.next
    print()
    
      
l1 = Queue(4)
l1.Enqueue(1)
l1.Enqueue(2)
l1.Enqueue(3)
l1.Enqueue(3)
l1.Enqueue(3)
l1.Enqueue(3)
# l1.Enqueue(3)
# l1.Enqueue(3)
# 
# l1.Dequeue()
# l1.Dequeue()
# l1.Dequeue()
# l1.Dequeue()
# l1.Enqueue(1)
# l1.Enqueue(2)
# l1.Enqueue(3)
# l1.Enqueue(3)
# l1.Enqueue(3)
# l1.Enqueue(3)
# print(l1.head.value)
# print(l1.j)
# l1.Dequeue()
# l1.Enqueue(3)
# l1.Enqueue(2)

l1.Print()
