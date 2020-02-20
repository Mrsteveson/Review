def isListPalindrome(l):
    # traverse the nodes of the linked list in the order they exist 
    # as we traverse, add the data of the current node to an array 
    # check if the contents of the nodes form a palindrome 
    # due to storing the nodes in a separate array, O(n) additional space 
​
    # is there a reverse method we could utilize? we'd have to write this
    # ourselves 
​
    # O(2*n) runtime 
    # O(1) space
    # can we utilize multiple pointers? 
    # figure out the length of the list 
    # figure out the midpoint 
    # we can advance a fast pointer to the midpoint 
​
    # at this point, fast will be at the midpoint, and the first half 
    # of the list will be doubly linked 
    # continue traversing fast to the end of the list 
    # at the same time, traverse another pointer in the opposite direction 
    
    # walk both halves of the list, checking if each element matches 
    # this assumes mutating the list is ok 
​
    # O(2*n) runtime 
    # O(n/2) space since we'd only need to copy the first half 
    # if mutating is not ok 
    # walk the input list, creating a reversed copy of the input as we go 
    # walk both lists in unison, checking that each of their elements matches


    # O(2*n) runtime 
# O(1) space
def isListPalindrome(l):
    # figure out the length of the list
    length = list_len(l)
    # ahead and behind pointers
    al = l
    bl = None
​
    # advance the ahead pointer to the midpoint of the list 
    for _ in range(length // 2):
        # while we're advancing the fast pointer, reverse the first
        # half of the list
        prev = al 
        al = al.next
        prev.next = bl
        bl = prev
    
    # check to see if we have a list with an odd number of nodes 
    if length % 2 == 1:
        al = al.next
​
    # traverse ahead and behind pointers in unison
    while al and bl:
        if al.value != bl.value:
            return False
        
        al = al.next
        bl = bl.next
​
    return True
​
def list_len(l):
    current = l
    counter = 0
​
    while current:
        counter += 1
        current = current.next
​
    return counter