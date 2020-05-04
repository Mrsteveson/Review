def has_cycle(head):
    # how can we tell if we've encountered a cycle? 
    # we can tell we have a cycle if we visit a node we've already visited before
    
    # O(n) runtime O(n) space 
    # use a map to hold all of the memory addresses of each node that we 
    # visit as we traverse the list 
    # as we iterate, check the map to see if the current node's address is in the map
    # if isn't, add its address to the map 
    # if it is, then we've found a cycle, return true 
    # otherwise return false
    
    # O(n) runtime, O(1) space, but we're mutating the input
    # add a 'visited' attribute to each node to designate that we've visited it 
    # before 
    # as we iterate, check to see if the current node has the visited attribute
    # if it doesn't, add the visited attribute to it 
    # if it does, then we've found a cycle, return true 
    # otherwise return false
    
    # O(n) runtime O(n) space 
    # variant of the 'visited' attribute strategy 
    # instead of mutating the list by adding attributes to each node, we could 
    # instead add each node to a set
    # on each iteration, check if the current node has already been added to the set 
    
    # O(n) runtime O(1) space
    # using fast and slow pointers 
    # init fast and slow pointers at the head of the list 
    fast = head
    slow = head 
    # fast pointer iterates twice as fast as the slow pointer 
    # iterate both pointers through our linked list so long as fast pointer 
    # hasn't reached the end of the list 
    # check whether the fast pointer has reached the end of the list or not
    while fast is not None and fast.next is not None:
      # update our pointers first since the runners need to start running
      slow = slow.next 
      fast = fast.next.next
      # if the pointers end up pointing at the same node, then we have a cycle 
      if fast == slow:
        return True
    # if the fast pointer reaches the end of the list, then no cycle 
    return False