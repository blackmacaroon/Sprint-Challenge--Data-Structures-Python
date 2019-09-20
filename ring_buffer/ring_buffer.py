class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #adds element to the buffer
    #if buffer is full, pop the oldest value
    pass

  def get(self):
    #return list of buffer elements in their given order
    #does not return None values, even if they are present
    pass