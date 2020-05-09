class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # the majority element is the element that appears more than floor(n/2) times 
        # we don't need to worry about there not being a majority element 
​
        # is there a possibility of multiple majority elements? looks like that's not possible 
        # what do we need to figure out? how many times each number shows up 
        # hash map with keys as the numbers and values as the counts 
        
        majority = len(nums) // 2
        
        # 1. populate a hash map with the counts of each of the numbers in the input list
        counts = {}
        
        for n in nums:
            if counts[n] is None:
                counts[n] = 1
            else:
                counts[n] += 1
  
			if counts[n] > majority:
                    return n
                
        # 2. look through our hash map to see which number has a value > n // 2
        # for key, values in counts.items():
        #     if values > majority:
        #         return key