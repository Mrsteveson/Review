def start_of_linked_list_cycle(head):
	# 1. figure out if there is a cycle 
	# 2. figure out the length of the cycle 
	# 3. move both pointers back to the beginning, jump one of the pointers ahead by the cycle 
	# length; move both pointers in unison until they meet 
​
	# unless the cycle starts at exactly halfway in the list, then fast and slow probably 
	# won't meet at the start 
​
	# multiple fast pointers that all traverse the list at different rates 
​
	# what information are we missing, or what do we need to figure out in order to adapt 
	# the fast and slow pointer idea? 
	# distance between the start of the list and the current node position 

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
​
def find_cycle_start(head):
  cycle_length = 0
  # find the LinkedList cycle
  slow, fast = head, head
  
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
	
    if slow is fast:
	  # calculate the length 
      cycle_length = calculate_cycle_length(slow)
      break
	
  return find_start(head, cycle_length)
​
def calculate_cycle_length(node):
  current = node
  cycle_length = 0
	
  while True:
    current = current.next
    cycle_length += 1
	
    if current == node:
      break
	
  return cycle_length
​
def find_start(head, cycle_length):
  # if there was no cycle, then cycle_length is 0
  if cycle_length == 0:
    return head 
	
  behind = head
  ahead = head
	
  # move ahead pointer forward 'cycle_length' nodes
  while cycle_length > 0:
    ahead = ahead.next
    cycle_length -= 1
	
  # increment both pointers until they meet at the start of the cycle
  while behind is not ahead:
    behind = behind.next
    ahead = ahead.next
	
  return behind
​
if __name__ == '__main__':
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
​
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))
​
  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))
​
  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))