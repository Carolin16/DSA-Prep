"""
   Q.1055 https://leetcode.com/problems/shortest-way-to-form-string/
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        T(N) : O(T^2 . S).
         Space Complexity - concatenated string is TS length
         in the worst case, we will have to concatenate source 
         string T times. Therefore,   concatenatedSource may consume O(TS) space.
        """

        """
            O(S) - all source char length
        """
        #create a set of source char
        sourceChar = set(source)

        """
            O(T) to check if all chars of target in source
        """
        #check if target char are same as source char
        for char in target:
            if char not in sourceChar:
                return -1
        
        concatStr = source
        minSubsequences = 1
        """
         loop runs until target is a subsequnece of concatenation
         O(N) : O(T^2 . S)
        """
        while not self.isSubsequence(concatStr , target):
            """
             concatenation = O(TS)
            """
            concatStr += source
            minSubsequences += 1
        return minSubsequences

    """
        O(N) : length of concatenated String -> T * S
        O(N) : O(TS)
    """
    def isSubsequence(self , source : str , target : str) -> bool:

        i = 0
        j = 0

        while i < len(source) and j < len(target):
            if target[j] == source[i] :
                j += 1
            i += 1

        return j == len(target)   
