def isListPalindrome(l):
    # palindrome: A string that doesn't change when reversed      
    # (it reads the same backward and forward).
​
    # the problem wants us to figure out if the elements in the linked 
    # list form a valid palindrome 
​
    # how would we check if a palindrome is valid in the first place?
​
    # what data structure to use to hold the nodes to make sure they
    # match? 
​
    # if we were using a stack, as we're traversing, push every node 
    # to the stack 
    # mark the ones we get to as visited and compare the ones we pop 
    # from the stack 
    # if all of those nodes match, then we have a valid palindrome 
​
    # now that we have a plan for checking if a palindrome is valid, 
    # how do we adapt that strategy to work on a linked list? 
​
    # O(2*n) runtime due to the two full traversals through the list 
    # O(n) additional space since we need to store the linked list values
    # separately in order to check against them 
    # 1. 
    # traverse the linked list from front to back, keeping track of 
    # each element as we traverse 
    # we can also set up previous pointers as we're traversing front
    # to back
    # we'll need to utilize extra memory to save every list element 
    # 1. 
    # traverse the linked list from back to front, checking if each 
    # element matches 
​
    # O(2*n) runtime since we need to figure out the length of the list 
    # and then perform another pass to check each list element 
    # O(1) additional space since all we do is check that each pointer's 
    # element matches the other's 
    # move outward in both directions from the central linked list node 
    # checking if each element matches 
    # 1. 
    # figure out the length of the linked list by traversing it entirely 
    # 0.5
    # once we know the length, move a pointer to the half-way point of 
    # the list, all the while, adding previous pointers to the first 
    # half of the list 
    # init another pointer at the middle element 
    # 0.5
    # have the pointers traverse in both directions, checking each 
    # element on each iteration 

def find_linked_list_length(l):
    current = l
    counter = 0
​
    while current:
        counter += 1
        current = current.next
​
    return counter
​
# O(2*n) runtime 
# O(1) space
def isListPalindrome(l):
    # figure out the length of the list
    length = find_linked_list_length(l)
    # ahead and behind pointers
    al = l
    bl = None
​
    # advance the ahead pointer to the midpoint of the list 
    for _ in range(length // 2):
        # while we're advancing the fast pointer, reverse the first
        # half of the list so that the first half of the list points
		# backwards
        prev = al 
        al = al.next
        prev.next = bl
        bl = prev
    
    # check to see if we have a list with an odd number of nodes 
    if length % 2 == 1:
		# if so, take the middle element as the later of the two
		# middle elements
        al = al.next
​
    # traverse ahead and behind pointers in unison, checking
	# each pointer's value
    while al and bl:
        if al.value != bl.value:
            return False
        
        al = al.next
        bl = bl.next
​
    return True