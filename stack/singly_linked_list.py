class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  def __str__(self):
    return f'Node: value-{self.value} next-{self.next}'
  def get_value(self):
    return self.value
  def get_next(self):
    return self.next
  def set_next(self, new_next):
    self.next = new_next

class LinkedList:
  # initiate list with one value
  def __init__(self, value=None):
    self.head = Node(value)
    self.tail = self.head
    self.size = 1
  def is_empty(self):
    return self.head == None
  def add_to_tail(self, value):
    # set head and tail to Node value if list is empty
    if self.is_empty():
      self.head = Node(value)
      self.tail = self.head
      return True
    elif self.head.value == None:
      self.head.value = value
      return True
    new_node = Node(value)
    self.tail.next = new_node
    self.tail = new_node
    self.size += 1
    return True
  def prepend(self, value):
    if self.is_empty():
      self.head = Node(value)
      self.tail = self.head
      self.size += 1
      return True
    if self.head.value == None:
      self.head.value = value
      return True
    new_node = Node(value)
    head = self.head
    new_node.next = head
    self.head = new_node
    self.size += 1
  def remove(self, value):
    if self.is_empty():
      raise Exception('Nothing to remove, list is already empty!')
    # if removed value is the head, set head to the next node
    if self.head.value == value:
      self.head = self.head.next
      self.size -= 1
      return value
    current_node = self.head
    while current_node != None:
      if current_node.next.value == value:
        current_node.next = current_node.next.next
        self.size -= 1
        return value
      current_node = current_node.next
  def remove_head(self):
    if self.is_empty():
      return None
    value = self.head.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
    self.size -= 1
    return value
  def get_nth_to_last(self, n):
    if self.is_empty():
      raise Exception('Whoops!  The list is empty!')
    left_node = self.head
    distance = 0
    right_node = self.head
    while right_node.next != None and distance < n - 1:
      right_node = right_node.next
      distance += 1
    if distance != n - 1:
      return None
    while right_node.next != None:
      left_node = left_node.next
      right_node = right_node.next
    return left_node.value
  def contains(self, value):
    if self.is_empty():
      return False
    current_node = self.head
    while current_node.next != None:
      if current_node.value == value:
        return True
      current_node = current_node.next
    if current_node.value == value:
      return True
    return False
  def get_max(self):
    if self.is_empty():
      return None
    elif self.size == 1:
      return self.head.value
    current_node = self.head
    current_max = self.head.value
    while current_node.next != None:
      if current_node.value > current_max:
        current_max = current_node.value
      current_node = current_node.next
    if current_node.value > current_max:
      current_max = current_node.value
    return current_max

# ---- From slack cs29_notepad, Sean Chen's implementation from lecture:
# class Node:
#   def __init__(self, value=None, next_node=None):
#     # the value at this linked list node
#     self.value = value
#     # reference to the next node in the list
#     self.next_node = next_node
#   def get_value(self):
#     return self.value
    
#   def get_next(self):
#     return self.next_node
    
#   def set_next(self, new_next):
#     # set this node's next_node reference to the passed in node
#     self.next_node = new_next
    
# class LinkedList:
#   def __init__(self):
#     # first node in the list 
#     self.head = None
#     # last node in the linked list 
#     self.tail = None
      
#   # O(1)
#   def add_to_head(self, value):
#     new_node = Node(value)
    
#     if not self.head and not self.tail:
#         self.head = new_node
#         self.tail = new_node 
#     else:
#         new_node.set_next(self.head)
#         self.head = new_node
        
#   # we have access to the end of the list, so we can directly add new nodes to it 
#   # O(1)
#   def add_to_end(self, value):
#     # regardless of if the list is empty or not, we need to wrap the value in a Node 
#     new_node = Node(value)
#     # what if the list is empty? 
#     if not self.head and not self.tail:
#       # set both head and tail to the new node 
#       self.head = new_node
#       self.tail = new_node
#     # what if the list isn't empty?
#     else:
#       # set the current tail's next to the new node 
#       self.tail.set_next(new_node)
#       # set self.tail to the new node 
#       self.tail = new_node
      
#     # we already have access to the head of the linked list, so we can directly remove from it 
#     # O(1)
#     def remove_from_head(self):
#       # what if the list is empty?
#       if not self.head:
#         return None
#       # what if it isn't empty?
#       else:
#         # we want to return the value at the current head 
#         value = self.head.get_value()
#         # remove the value at the head 
#         # update self.head 
#         self.head = self.head.get_next()
#         return value
            
#     # iterate over our linked list and print out each value in it 
#     def print_ll_elements(self):
#       current = self.head
      
#       while current is not None:
#         print(current.value)
#         current = current.get_next()

# ​ll = LinkedList()
# ll.add_to_head(3)
# ll.add_to_head(5)
# ll.add_to_head(9)
# ll.add_to_head(11)
