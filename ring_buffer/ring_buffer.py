class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0  #look at this as the index, keeping track of storage  x _ x x x | x x _ x x | x x x _ x | x x x x _ | full? "delete" the old one  _ x x x x |
    self.storage = [None]*capacity

  def append(self, item):
    #add item to buffer
    #add to storage at current index
    self.storage[self.current] = item
    #increment index
    self.current += 1
    #until index == capacity
    if self.current == self.capacity:
      #reset current to 0 / debug "list assignment out of range" because i had current == 0, instead of = 0
      self.current = 0

  def get(self):
    #return list
    ring_buffer = []
    #return list of buffer elements in their given order
    for i in self.storage:
      #does not return None values, even if they are present
      if i is not None:
        #append i to list
        ring_buffer.append(i)
    return ring_buffer