class Node(object):
  def __init__(self,value):
    self.value = value
    self.next = None

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
  
  def InsertatFirst(self,value):
    n = Node(value)
    x = self.head
    if x == None:
      self.head = n
      self.tail = n
    else:
      n.next = self.head
      self.head = n

  def Tail(self):
    return self.tail.value
  
  def Print(self):
    x = self.head
    while x:
      print(x.value,end=' --> ')
      x = x.next
    print()
  
  def Find(self,value):
    x = self.head
    i = 0
    while x:
      if x.value == value:
        return f"{x.value} present at {i+1} node"
      i+=1
      x=x.next
    return None
      

  def InsertatEnd(self,value):
    n = Node(value)
    x = self.tail
    if x == None:
      self.head = n
      self.tail = n
    else:
      x.next = n
      self.tail = n
      self.tail.next = None

  def Insertafter(self,item,value):
    n = Node(value)
    x = self.head
    y = self.head.next
    # print(x.value)
      
    while item!= x.value:
      x = x.next
      y = y.next
    # else:
    #   print('Element Not Found')

    if item == x.value and y is not None:
      x.next = n
      n.next = y
      # print(self.tail.value)
    elif item == x.value and y is None:
      x.next = n
      self.tail = n
      n.next = y
      self.tail.next = None
    


  def DeleteatFirst(self):
    x = self.head
    if x is not None:
      self.head = self.head.next  
      x = None
    else:
      print('LList is empty')

  def DeleteatEnd(self):
    x = self.head
    y = self.tail
    if x is not None:
      while x.next.next !=None: 
        x = x.next
      self.tail = x
      self.tail.next = None
    else:
      print('LList is empty')
  
  def DeletebyValue(self,value):
    w = self.head
    x = self.head
    y = self.head.next
    
    i = 0
    while x.value !=  value:
      i=i+1
      if i > 1:
        w = w.next
        
      x = x.next
      
      y = y.next
    
    if value == x.value and y is not None and i == 0:
      self.head = y
      w = None
      x = None
    elif value == x.value and y is not None and i != 0:
      w.next = y
      x = None
    #   w.next = y

    elif value == x.value and y is None and i != 0:
      x = None
      w.next = y
      self.tail = w
    
      

# a = LinkedList()
# a.InsertatFirst(2)
# a.InsertatFirst(3)
# a.InsertatLast(4)
# a.InsertatLast(31)
# a.DeletebyValue(4)
# a.DeletebyValue(2)
# a.Print()
L1 = LinkedList()
L1.InsertatFirst(2)
L1.InsertatFirst(3)
L1.InsertatEnd(4)
L1.Insertafter(2,5)
L1.DeletebyValue(4)
L1.Print()
