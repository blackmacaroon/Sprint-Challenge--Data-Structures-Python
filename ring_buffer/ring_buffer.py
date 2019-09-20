class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #adds element to the buffer
    #if buffer is full, remove the oldest value
    pass

  def get(self):
    #return list of buffer elements in their given order
    for i in self.storage:
      #does not return None values, even if they are present
      if i is not None:
        return i