
class Node(object):
  def __init__(self,value):
    self.value = value
    self.next = None
    self.prev = None

class doublyLinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
  
  def InsertatFirst(self,value):
    n = Node(value)
    x = self.head
    # y = self.tail
    if x is None:
      self.head = n
      self.tail = n
    else:
      n.next = self.head
      x.prev = n
      self.head = n
      self.head.prev = None

  def InsertatEnd(self,value):
    n = Node(value)
    x = self.tail
    if x is None:
      self.head = n
      self.tail = n
    else:
      self.tail.next = n
      n.prev = self.tail
      n.next = None
      self.tail = n
    return
  def search(self,item):
    x = self.head
    while x:
      if x.value == item:
        return True
      x = x.next
    return False
  
  def Insertafter(self,item,value):
    x = self.head
    y = self.head.next
    n = Node(value)
    if not self.search(item):
      return print('not present')
    else:
      while item!= x.value:
        x = x.next
        y = y.next


      if item == x.value and y is not None:
        x.next = n
        n.next = y
        n.prev = x
        y.prev = n

      elif item == x.value and y is None:
        x.next = n
        self.tail = n
        n.next = y
        n.prev = x
        self.tail.next = None


  def Tail(self):
    return self.tail.value

  def Head(self):
    return self.Head.value

  def Find(self,value):
    x = self.head
    i = 0
    while x:
      if x.value == value:
        return f"{x.value} present at {i+1} node"
      i+=1
      x=x.next
    return None

  def DeleteatFirst(self):
    x= self.head
    if x is not None:
      self.head = x.next
      self.head.prev = None
      x = None
    else:
      print('list is empty')
    
  def DeleteatEnd(self):
    x = self.tail
    
    if x and x.prev is not None :
      self.tail = x.prev
      self.tail.next = None
    elif self.head == self.tail:
      self.tail = None
      self.head = None
      print('LList is empty')
    
  def DeletebyValue(self,value):
    w = self.head
    x = self.head
    y = self.head.next
    if not self.search(value):
      return print('not present')
    else:
      i = 0
      while x.value !=  value:
        i=i+1
        if i > 1:
          w = w.next
          
        x = x.next
        
        y = y.next
      
      if value == x.value and y is not None and i == 0:
        print(w.value)
        print(x.value)
        print(y.value)
        self.head = y
        w = None
        x = None
        self.head.prev = None
      elif value == x.value and y is not None and i != 0:
        w.next = y
        x = None
        y.prev = w

      elif value == x.value and y is None and i != 0:
        x = None
        w.next = y
        self.tail = w
      elif self.head == self.tail:
        self.head = None
        self.tail = None
      
    
      
    return
    
  def Print(self):
    x = self.head
    while x:
      print(x.value,end=' <---> ')
      x = x.next
    print()


l1 = doublyLinkedList()
l1.InsertatFirst(1)
l1.InsertatFirst(2)
l1.InsertatFirst(3)
l1.InsertatEnd(0)
l1.InsertatEnd(21)
l1.DeletebyValue(21)
l1.InsertatEnd(0)
l1.InsertatFirst(21)
l1.InsertatEnd(21)
print(l1.Find(1))
l1.Print()
