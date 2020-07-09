class Solution:
    def isMatch(self, s: str, p: str)-> bool:
        # use a dynamic programming approach 
        # think of DP as recursion that is augmented with caching 
        cache = {}
        
        def recurse(s, p):
            # first just think of this with plain old recursion
            # what are our base cases? 
            # base case 1: if the string s is empty 
            if not s:
                # s = "", p = ""
                # if the pattern is empty, "*", True
                # s = "", p = " "
                # if the pattern is not empty, "?" False 
                # s = "", p = "*"
                return (p == '') or (p[0] == '*' and recurse(s, p[1:]))
            # base case 2: if the pattern is empty
            if not p:
                # p = "", then s = "", True
                # else, False 
                return (s == '')
            
            # also check the cache 
            if (s, p) not in cache:
                # handling asterisks in pattern 
                # what happens when p[0] == '*'? 
                if p[0] == '*':
                    # match any number of chars
                    # or match the empty sequence 
                    # recurse twice, one way that increments the string 
                    # the other way incrementing the pattern 
                    # if any recursive come back True, return True 
                    cache[(s, p)] = recurse(s, p[1:]) or recurse(s[1:], p)
                # otherwise, p[0] != "*"
                else:
                    # compare the first chars of s and p
                    # if they don't match or p[0] != '?'
                    # return False
                    if s[0] != p[0] and p[0] != '?':
                        cache[(s, p)] = False
                    # if we've recursed all the way through both strings
                    # with no mismatches between string and pattern, return True
                    else:
                        cache[(s, p)] = recurse(s[1:], p[1:])
            
            return cache[(s, p)]
        
        return recurse(s, p)
​
#         def recurse(s, p):
#             # first just think of this with plain old recursion
#             # what are our base cases? 
#             # base case 1: if the string s is empty 
#             if not s:
#                 # s = "", p = ""
#                 # if the pattern is empty, "*", True
#                 # s = "", p = " "
#                 # if the pattern is not empty, "?" False 
#                 # s = "", p = "*"
#                 return p == '' or p[0] == '*' and recurse(s, p[1:])
#             # base case 2: if the pattern is empty
#             if not p:
#                 # p = "", then s = "", True
#                 # else, False 
#                 return s == ''
            
#             # also check the cache 
#             # handling asterisks in pattern 
#             # what happens when p[0] == '*'? 
#             if p[0] == '*':
#                 # match any number of chars
#                 # or match the empty sequence 
#                 # recurse twice, one way that increments the string 
#                 # the other way incrementing the pattern 
#                 # if any recursive come back True, return True 
#                 return recurse(s, p[1:]) or recurse(s[1:], p)
#             # otherwise, p[0] != "*"
#             else:
#                 # compare the first chars of s and p
#                 # if they don't match or p[0] != '?'
#                 # return False
#                 if s[0] != p[0] and p[0] != '?':
#                     return False
#                 # if we've recursed all the way through both strings
#                 # with no mismatches between string and pattern, return True
#                 return recurse(s[1:], p[1:])
    
#         return recurse(s, p)

class Solution:
    def isMatch(self, s: str, p: str)-> bool:
        cache = {}
        
        def recurse(s, p):
            if not s:
                return (p == '') or (p[0] == '*' and recurse(s, p[1:]))
            if not p:
                return not s
​
            if (s, p) not in cache:
                if p[0] == '*':
                    cache[(s, p)] = recurse(s, p[1:]) or recurse(s[1:], p)
                else:
                    if s[0] != p[0] and p[0] != '?':
                        cache[(s, p)] = False
                    else:
						# instead of incrementing along both string and pattern via recursion
						# we can cut down on recursive calls by incrementing manually so long 
						# as both the current string and pattern chars are normal letters or '?'
                        sp, pp = 0, 0
                        
                        while sp < len(s) and pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                            sp += 1
                            pp += 1
                        
                        if sp == len(s) and pp == len(p):
                            cache[(s, p)] = True
                        else:
							# we encountered an '*' in pattern, recurse as normal
                            cache[(s, p)] = recurse(s[sp:], p[pp:])
            
            return cache[(s, p)]
        
        return recurse(s, p)