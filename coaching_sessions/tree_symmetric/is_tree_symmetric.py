# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def print_tree(self, root):
        if not root:
            return
        print(root.val)
        self.print_tree(root.left)
        self.print_tree(root.right)
    
    
    # in_order_traversal needs to preserve empty subtrees 
    def in_order_traversal(self, root, output):
        if not root:
            output.append("dead end")
            return
        if root.val == 'null':
            output.append(None)
            return
        # traverse the left subtree 
        self.in_order_traversal(root.left, output)
        # access the data element 
        output.append(root.val)
        # traverse the right subtree 
        self.in_order_traversal(root.right, output)
    
    def is_list_palindrome(self, arr):
        # have two pointers on opposite ends of the list 
        left = 0
        right = len(arr) - 1
        # walk both pointers towards the middle of the list
        # check <= for lists with an odd number of elements 
        while left <= right:
            # checking each element to see if they match 
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True 
    
    def isSymmetric(self, root: TreeNode) -> bool:
        # traverse the tree 
        # how would we traverse the tree to generate this list? 
        # store the data in a list?
    
        # check to see if the data 
        
        # [3, 2, 4, 1, 4, 2, 3]
        # check if this list is a palindrome 
        
        output = []
        
        # 1. perform an in-order traversal of the tree nodes 
        # reverse order traversal would also work 
        # dump the node values into a list 
        self.in_order_traversal(root, output)
        
        print(output)
        
        # 2. check if the list elements constitute a palindrome 
        return self.is_list_palindrome(output)
        
 
        # similar to checking if two binary trees are equal 
        # at every recursive call, what we're checking for is 
        # if the right is symmetrical to the left and the left is
        # symmetrical to the right, and that the values match 
        
        # define a flip function that creates a mirrored clone of the input tree 
        # check if the original tree and the flipped tree are equal 
​
        # perform two breadth-first searches, both in opposite directions
        # output the results to two separate arrays 
        # check if the two arrays match

from collections import deque
​
def isSymmetric(self, root: TreeNode) -> bool:
	# use a queue to facilitate breadth first search
	q = deque()
	
	# for each iteration, we dequeue two nodes at a time, so 
	# we'll need to add the root twice 
	q.append(root)
	q.append(root)
	
	while len(q) > 0:
		r1 = q.popleft()
		r2 = q.popleft()
		
		# we can't say anything definitive if both nodes 
		# are None; just move on to the next iteration 
		if r1 is None and r2 is None:
			continue
		
		if r1 is None or r2 is None:
			return False
​
		if r1.val != r2.val:
			return False
		
		# append the next set of nodes 
		q.append(r1.left)
		q.append(r2.right)
​
		q.append(r1.right)
		q.append(r2.left)
​
	return True