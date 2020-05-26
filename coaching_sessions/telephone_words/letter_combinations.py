def letterCombinations(self, digits: str) -> List[str]:
        # how do we determine whether we need a recursive implementation or not? 
        # how do we decide whether we should re-use the same initial function for 
        # our recursion, or define a new helper function? 
        # what do we need to keep track of in order to recurse? 
        # how do we make sure that the recursive call moves us towards one of the base cases? 
        
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def helper(current_combination, leftover_digits):
            # if there is no more digits to check
            if len(leftover_digits) == 0:
            # if len(current_combination) == len(digits):
                # the combination is done
                output.append(current_combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                letters = phone[leftover_digits[0]]
                for letter in letters:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    helper(current_combination + letter, leftover_digits[1:])
                    
        output = []
        
        if digits:
            helper("", digits)
            
        return output