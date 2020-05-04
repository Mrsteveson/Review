def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # init an ouptut array 
        output = []
        left = 0
        right = k - 1
        
        # loop through the array 
        while right < len(nums):
            # get the subarray of size k, starting from the left side 
            subarray = nums[left:right+1]
            
            # find the max value in the subarray
            # add the max value to the ouptut array 
            output.append(max(subarray))
            
            # increment both left and right pointers
            left += 1
            right += 1
        
        # return the output array 
        return output
            
    # how can we compute the max value in a subarray in a less redundant fashion? 
    # is there a data structure we could use? 
    # binary search tree 
    # that would make fetching the max straightforward
    # removing an element from a binary search tree is not that easy 
    
    
    # use a queue to maintain proper ordering of the elements in the sliding window as we iterate 
    # along them 
    # to make figuring out the max value easy, maintain the rule that the first element in the 
    # queue must be the max value in the queue 
    # so that means that when a new element that comes in is > queue[0], kick out elements 
    # from the front of the queue until the head of the queue > the new incoming element 
    # set the new larger element as the max value 
    # each time the window slides, add the first queue element to the output array

from collections import deque
​
def sliding_window_max(nums, k):
	output = []
	q = deque()
	
	for i, val in enumerate(nums):
		# pop values from our queue until the max value is at the 
		# front of the queue
		while len(q) > 0 and val > q[-1]:
			q.pop()
			
		q.append(val)
		
		# index to keep track of the left index of the window
		left_idx = i - k + 1
		
		# so long as the left side of the window is in bounds
		if left_idx >= 0:
			output.append(q[0])
			
			# check if the element at `left_idx` is the head of the queue
			# we need to remove it if is
			if nums[left_idx] == q[0]:
				q.popleft()
				
	return output