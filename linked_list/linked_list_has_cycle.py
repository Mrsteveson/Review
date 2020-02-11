"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.
​
A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
​
​
def has_cycle(head):
    # traverse the list recursively/iteratively 
      # can we count the number of edges that refer to each node 
      # if we see that a node has more than one edge referring to it, then 
      # we've found a cycle 
        # figuring out how to count references to a node 
        
    # if we're allowed to mutate the input 
    # as we traverse the list, can we add an attribute to each node to mark 
    # that it's been visited? 
      # if we end up iterating along a list with a cycle, then we'll encounter 
      # a node we've already visited before, thus there's a cycle 
      
    # add each node (a memory address where the node resides) to a set 
      # as we're traversing, if we run into a node that is already in the set,
      # then that also tells us we have a cycle 
      
    # if we make a copy of the list first and then mutate the copy, is that considered
    # mutating the original data? No, we're not mutating the original data. 
      
    # assume that node data values are not unique 
    
    # how would we solve this without being able to mutate the input list, and 
    # with O(1) space complexity? 
    
    # fast and slow pointers 
    # using multiple pointers when working with linked lists to implement a more 
    # efficient traversal through a linked list problem 
    if not head:
      return False 
    
    fast = head
    slow = head 
      
    # have the fast pointer traverse twice as fast as the slow pointer 
    # keep iterating so long as fast.next is a valid node 
    while fast and fast.next:
      fast = fast.next.next 
      slow = slow.next 
      
      # check if fast and slow references are referring to the same memory address 
      if fast is slow: 
        return True 
      
    # if we reach the end of the loop, that means that we reached the end of the list 
    return False 
