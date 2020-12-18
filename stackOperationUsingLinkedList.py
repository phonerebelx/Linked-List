


class Node(object):
  def __init__(self,value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.tail = None
  def isempty(self):
    empty = True if self.head == None else False
    return empty

  def push(self,value):
    n = Node(value)
    x = self.head
    # y = self.tail
    if x == None:
      self.head = n
    else:
      n.next = self.head
      self.head = n

  def pop(self):
    x = self.head
    if not self.isempty():
      self.head = x.next
      x = None
    else:
      self.head = None
      print('UnderFlow')
    
  def Peek(self):
    peek_value=self.head.value if not self.isempty() else None
    return peek_value

      

  def Print(self):
    x = self.head
    if not self.isempty():
      while x:
        print(x.value,end=' --> ')
        x=x.next
      print()
    else:
      print('Stack is empty')




l1 = Stack()
l1.push(4)
l1.push(1)
l1.push(11)
# l1.pop()
# l1.pop()
print(l1.Peek())
l1.Print()

