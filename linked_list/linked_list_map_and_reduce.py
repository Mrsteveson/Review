def array_map(arr, fn):
  output = []
  # loop through the array elements 
  for x in arr:
    # apply fn to the current element 
    updated = fn(x)
    # add the updated element to an output array
    output.append(updated)
  # return the output array
  return output
​
l = [1, 2, 3, 4, 5, 6]
# print(array_map(l, lambda x: x + 1))
​
class ListNode:
  def __init__(self, val):
    self.value = val
    self.next = None
​
# take in a linked list as input
# do we return an array
# or do we return a linked list?
# returns a new linked list of the mapped values 
def linked_list_map(head, fn):
  # output will be a new linked list instead 
  # init output to be a dummy node 
  dummy = ListNode(-1)
​
  output = dummy
  # loop through the input linked list 
  current = head
  while current:
    # update the current element with the fn
    updated = fn(current.value)
    # add a new linked list node with the updated 
    # element to our output linked list 
    output.next = ListNode(updated)
    current = current.next 
    output = output.next
    
  # return the output linked list  
  return dummy.next
​
ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
​
mapped = linked_list_map(ll, lambda x: x + 1)
​
def print_linked_list(head):
  current = head 
  while current:
    print(current.value)
    current = current.next
​
# print_linked_list(mapped)
​
# what does the passed-in fn look like? 
# lambda current, next: current + next
def array_reduce(arr, fn, init=None):
  starting_idx = 0
  answer = init
​
  if init is None:
    starting_idx = 1
    answer = arr[0]
​
  for x in arr[starting_idx:]:
    answer = fn(answer, x)
​
  return answer
​
# print(array_reduce([1, 2, 3, 4, 5, 6], lambda current, next: current + next, 10))
​
# reduce doesn't need to return a new linked list 
def linked_list_reduce(head, fn, init=None):
  answer = init
  current = head 
​
  if init is None:
    answer = head.value
    current = current.next
​
  while current:
    answer = fn(answer, current.value)
    current = current.next
​
  return answer
​
ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
​
print(linked_list_reduce(ll, lambda current, next: current + next, 10))