def sortedInsert(head, data):
  # create our DLL node 
  new_node = DoublyLinkedListNode(data)
  # what's the base case(s)?
  # we also have to check if there is no head 
  if not head:
    return new_node
  if data < head.data:  
    # insert it before the head
    new_node.next = head 
    head.prev = new_node 
    return new_node
  # if we aren't in the base case, how do we get there? 
  else:
    # there is a head and data > head.data 
    rest = sortedInsert(head.next, data)
    # hook up the rest of the list with the head 
    head.next = rest 
    rest.prev = head 
    return head