# Is it a valid binary search tree?

# traverses the tree in-order
# returns the node values in an array 
def in_order_traverse(root, arr=[]):
  if root.left: 
    in_order_traverse(root.left, arr)
  arr.append(root.data)
  if root.right:
    in_order_traverse(root.right, arr)
​
# return a boolean indicating whether the array is 
# in sorted ascending order 
def is_sorted(arr):
  for i in range(1, len(arr)):
    if arr[i] <= arr[i-1]:
      return False 
  return True 
​
def checkBST(root):
  # have a previous pointer that keeps track of the grandparent's value 
  # push every tree node value into an array so that we can check previous generations
  
  # traverse through the tree 
  # if there is a right but its value < its parent, then that's not valid 
  # if there is a left but its value > its parent, then that's not valid 
  # we might very well have to check past just a single generation 
    # how do we do that? 
    # we could keep traversing backwards up the tree to check earlier generations?
    
    # how do we check non-local values? 
  
  tree_values = []
  # traverse the tree in-order, add the elements to an array 
  in_order_traverse(root, tree_values)
  
  # check that the elements are sorted 
  return is_sorted(tree_values)
​
​
def helper(root, min, max):
  # base cases:
  # if we have an empty tree 
  if root is None:
    return True 
  if root.data <= min or root.data >= max:
    return False 
  # recurse step: 
  # recurse on left child and recurse on right child 
  return helper(root.left, min, root.data) and helper(root.right, root.data, max)
​
def checkBST(root):
  return helper(root, float("-inf"), float("inf"))