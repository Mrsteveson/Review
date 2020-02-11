class SkipNode:
  # is a node just an individual square, or is it the entire station? 
  # if we opt for the station representation, then we could represent it 
  # as a list of pointers to the next station 
  def __init__(self, elem=None):
    self.elem = elem 
    # self.stations holds pointers to the next station
    # index 0 will always hold the pointer to the next local station 
    # indices after that will point to express stations 
    self.stations = []
    # what about the height? 
​
    # "square" representation 
    self.prev = None 
    self.next = None 
    self.below = None 
    self.above = None 
​
class SkipList:
  def __init__(self, max_height):
    # should have pointers to every single station in the first node 
    self.max_height = max_height
    self.head = [SkipNode() for i in range(max_height)] 
    # connect all of the nodes
    # loop through all of the nodes in the head 
    if len(self.head) > 1:
      for i in range(max_height):
        # for the ith node, connect its "below" to the i-1th node 
        if i == 0:
          self.head[i].above = self.head[i+1]
        # connect its "above" to the i+1th node 
        elif i == len(self.head) - 1:
          self.head[i].below = self.head[i-1]
        else:
          self.head[i].above = self.head[i+1]
          self.head[i].below = self.head[i-1]
​
  def search(self, target):
    # start at the last node in self.head 
    current = self.head[-1]
    # if below exists go there 
    while current.below: 
      current = current.below
      # go right if next < target 
      while target >= current.next:
        current = current.next
​
    return current 
​
    # start at the top node in the head 
    # check if the next node along this line > target 
      # move down a layer 
      # check if the next node along this line > target 
      # if the next node along the line <= target 
        # move right to the next node 
          # stop criteria
            # we found the element in our current line 
      
  def insert(self, val):
    # search the skip list for the largest value < val (assuming the value 
    # doesn't already exist in the list)
    # create a new node with the val and connect it to the found node 
    # add layers to this new node by flipping coins to determine how many 
    # layers it gets 
    # connect those layers up to nodes in the same layer 