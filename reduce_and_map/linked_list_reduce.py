# reduce takes a data structure and either finds a key piece of data or 
# be able to restructure the data structure 
​
# 1. Reduce usually takes a linear data structure (99% we use reduce on an array)
# 2. Reduce "aggregates" all of the data in the data structure into one final value 
# 3. Reduce is extremely flexible with how the reduction actually happens 
# 3a. Reduce doesn't care how the reduction happens 
# 4. The "reducer" function that's passed in as input is how we specify how the reduction happens 
​
# what's the deal with the anonymous function's parameters? 
# 1. An aggregator value 
# 2. The current list node 
# 3. An optional value the aggregator is initialized with 
​
# what happens on a single call of the anonymous function? 
# how many times does the reducer function get called? Once for every element in our data structure 
# does the anonymous function do the work of iterating over our data structure? 
# no, the anonymous function itself doesn't do the work of iterating 
​
​
# Steps for our reduce function 
​
​
# How do all of these calls get aggregated into a single value? 
# The anonymous function needs to update the aggregated value somehow
​
# where is the state set and how is it defaulted to the head? 
​
def linked_list_reduce(head, reducer, init=None):
  # where/when do we initialize the state? 
  # initialize state before we start looping 
  state = None 
  # what do we do when the init value is set? 
  if init != None: 
    state = init 
  # what do we do when the init value is None? 
  elif state is None:
    # set the state to be the first value in our list 
    state = head.value
    # move the head to the next list node 
    head = head.next  
  # 1. Loop over the data structure 
  current = head 
​
  while current:
    # 2. Call our anonymous function on the current iteration value
    # 3. Update our state to be the result of the anonymous function
    state = reducer(state, current.value)
    # update our current pointer 
    current = current.next  
  # 4. Return the final aggregated state
  return state  
​
​
class Node:
  def __init__(self, value, next=None):
    self.value = value 
    self.next = next
​
l1 = Node(4)
l2 = Node(7)
l3 = Node(15) 
l4 = Node(29)
l5 = Node(5)
​
l1.next = l2 
l2.next = l3
l3.next = l4 
l4.next = l5 
​
reducer = lambda x, y: x - y 
​
print(linked_list_reduce(l1, reducer, 100))