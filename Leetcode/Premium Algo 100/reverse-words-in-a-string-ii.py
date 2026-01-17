"""
    Mistakes : missed return type for helper functions
    Time complexity: O(N), it's two passes along the string.
    Space Complexity : O(1)

    Q 182 : https://leetcode.com/problems/reverse-words-in-a-string-ii/
"""
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #reverse whole string
        self.reverseString(s,0,len(s) - 1)
        #reverse word by word
        self.reverseWord(s)

    def reverseString(self, s:List[str], start:int,end:int)-> None: 
        while start < end:
            s[start],s[end] = s[end],s[start]
            start += 1
            end -=1

    def reverseWord(self,s:List[str])-> None:
        start = 0
        end = 0

        while start < len(s):
            while end < len(s) and s[end] != " ":
                end += 1
            
            self.reverseString(s,start,end - 1)
            start = end + 1
            end += 1
        
