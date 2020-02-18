def findMergeNode(head1, head2):
  # we want to return the integer value of the node where the lists merge 
  # presumably we can compare pointers 
  # going down both lists and finding repeated pointer values 
​
  # is each node unique? 
  # we can assume that each node instance is unique 
​
  # how do we determine that a node is the merge point? 
​
  # we need to somehow keep track of which nodes we've visited before 
  # after we've iterated through one of the linked lists 
​
  # adding every node from one of the lists to the hashmap will be linear 
  # in the length of that linked list 
  # the loop through the other linked list will be linear in the length of 
  # that linked list 
  # O(m + n) where n is the length of the first linked list and m is the 
  # length of the second linked list 
  # O(n) space complexity since we're storing all of one linked list in a 
  # hashmap 
  # init a hashmap which will keep track of which nodes we've seen before 
  # loop through one of the lists, and add each node to the hashmap 
  # so now every node in the hashmap is one we've visited before 
  # loop through the other list, checking if the current node is in 
  # the hashmap 
  # the first node we encounter that is already in the map is the merge 
  # point 
​
  # O(n) where n is the length of the longer list 
  # loop through both lists at the same time 
  # we can check if either of the two current nodes has been visited before 
  # as soon as we see one that has been visited before, then we've found 
  # the merge point 
​
  # instead of using a hashmap, can we instead just mark each node that 
  # we've visited before? Add a 'visited' attribute to each node in the 
  # first list as we loop through it
  # when we loop through the second list, we can check each node to see if 
  # it has this 'visited' attribute 
​
  # initializing current pointers 
  curr_a = head1 
  curr_b = head2 
​
  # loop through one of the lists, adding a attribute to each node 
  while curr_a:
    curr_a.visited = True 
    curr_a = curr_a.next 
​
  # loop through the other list, checking for the first node that 
  # has the attribute 
  while curr_b: 
    if hasattr(curr_b, 'visited'): 
      return curr_b.data 
    curr_b = curr_b.next