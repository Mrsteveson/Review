#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
  # can you come up with a recursive solution? 
​
  # 1. go through each list node 
  # 2. swap the previous and the next for each node 
  # 3. handle edge cases 
      # empty list - return None 
      # 1-element list? perform the swapping and return the same node 
  current = head 
  # new_head = head
  # what's the stopping criteria? 
  while current: 
    # when current is None, that's when we stop iterating 
    true_next = current.next 
    # swap prev and next pointers 
    current.next = current.prev 
    current.prev = true_next 
    # update our current pointer to the next node 
    head = current 
    current = true_next
​
  return head