"""
    T(n) : O(n)
    Space Complexity : O(min(m , n ))
    m is length of charset
    n is length of string
    Q 3:https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        right = 0
        maxlen = 0

        while right <= len(s)-1:
            if s[right] not in charSet:
                charSet.add(s[right])
                maxlen = max(maxlen , right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
            right += 1
    

        return maxlen
        
        
