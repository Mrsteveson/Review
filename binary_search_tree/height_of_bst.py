def height(root):
  return traverse(root)
  # depth first search, keep a height counter 
​
  # DFS is probably preferred over BFS since we'll reach the leaves of 
  # the tree sooner 
​
  # recursively or iteratively? 
​
  # iterative approach 
  # count = 0
  # max_height = 0
  # stack for LIFO ordering 
  # in a while loop, check if the stack still has nodes 
    # pop from the stack 
    # if the popped off node has children 
      # add them to the stack 
    # increment our counter 
    # if the popped off node doesn't have children
    # then we've figured out the height of this branch 
    # compare the count to max_height and keep the larger value 
​
    # when/how do we check when we have a new max height? 
    # how we do always correctly "backtrack" the counter to the correct value? 
​
  # recursive approach 
  # how does this recursive approach solve the backtracking issue 
  # we were seeing with the iterative version? 
​
# side note: if you're solving a problem recursively but the function 
# doesn't provide you with all of the parameters you need, make a new 
# function. The new function will be your recursive function, and then 
# you just need to call this recursive function in the "main" function. 
def traverse(root, height=0):
  left_height = 0
  right_height = 0
  # where does a counter fit into this recursive implementation? 
  # base case: if the current node has no children 
  if not root.left and not root.right:
    return height 
  # the current node has at least one child 
  # if the current node has a right child
  if root.right:
    # increment height counter 
    height += 1
    # call this function recursively on the right child 
    right_height = traverse(root.right, height)
  # if the current node has a left child 
  if root.left:
    # increment height counter 
    height += 1
    # call this function recursively on the left child 
    left_height = traverse(root.left, height)
​
  return max(right_height, left_height) 