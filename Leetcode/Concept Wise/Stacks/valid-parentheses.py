"""
Q.20 https://leetcode.com/problems/valid-parentheses/
Time Complexity : O(n) We traverse the string exactly once. 
Each character involves a stack push or pop, which are both O(1) operations.
Space Complexity : O(n) In the worst case (e.g., a string of all opening brackets like ((((((), 
the stack will grow to the same size as the input string.
"""

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dictToCheck = dict(( '()' , '{}' , '[]'))
        paramtoCheck = '{(['

        for char in s:
            if char in paramtoCheck:
                stack.append(char)
            """
            # Key: Opening Bracket -> Value: Closing Bracket
                dictToCheck = {
                    '(': ')',
                    '{': '}',
                    '[': ']'
                }
                            """
            elif len(stack) == 0 or char !=  dictToCheck[stack.pop()]:
                return False
        
        return len(stack) == 0
        
