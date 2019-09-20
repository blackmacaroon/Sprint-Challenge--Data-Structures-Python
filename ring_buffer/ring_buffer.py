class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #if storage length < capacity, add the item
    if len(self.storage) < self.capacity:
      self.storage[self.current] = item
    #while current < capacity-1
    if self.current < self.capacity -1:
      print("yo")
    #adds element to the buffer
    #if buffer is full, remove the oldest value (fifo)
    

  def get(self):
    #return list of buffer elements in their given order
    for i in self.storage:
      #does not return None values, even if they are present
      if i is not None:
        return i