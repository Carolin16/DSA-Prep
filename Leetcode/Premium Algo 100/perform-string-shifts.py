"""
Let L be the length of the string and N be the length of the shift array.

Time complexity : O(N⋅L).

Making a single modification to the input string has a cost of O(L), as we need to create a new string with the modifications. We are making one modification for each shift operation. As there are N shift operations, this gives us a total time complexity of O(N⋅L).

Space complexity : O(L).

While performing a string modification, we'll have both the original string and the new string in memory. Therefore, the space complexity is O(L).
 Q.1427 https://leetcode.com/problems/perform-string-shifts/

"""

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        #0 left shift
        #1 right shift
        # amount
        #strings are immutable - we cannot modify it
        #a new string needs to be created for every shift

        #modulo for string shifting is needed Because shifting 
        #more than the string length is redundant.

        for direction,amount in shift:
            amount = amount%len(s)

            if direction == 0:
                #abcde amount = 2
                #shift[amount:] cde + shift[:amount] ab => cdeab
                s = s[amount:] + s[:amount]
            else:
                #Take characters from the end and move them to the front
                # 0   1   2   3   4   5
                # a   b   c   d   e   f
                #-6  -5  -4  -3  -2  -1
                s = s[-amount:] + s[:-amount]
    
        return s
        
