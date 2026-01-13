"""
Let L be the maximum number of digits n can have (L=log 
10
​
 n).

Time complexity: O(L)

Since the input number n has L digits, it requires O(L) time to iterate over and convert each digit of n, then O(L) again to reverse the result. Note that string is immutable in python, so we add each digit to a list, and convert the final list of digits to the string, which is a process that costs O(L).

Space complexity: O(L)

We create an object of length L, same as the number of digits of n.

This formula is a way of saying that the number of digits in a number is directly related to its logarithm (base 10).In programming and math, we often need to know how "long" a number is (the number of digits) to determine how many times a loop must run or how much memory to allocate.Why $\log_{10}$?The base-10 logarithm asks the question: "10 raised to what power gives me this number?"$\log_{10}(10) = 1$$\log_{10}(100) = 2$$\log_{10}(1,000) = 3$Notice the pattern: the result of the log is roughly one less than the number of digits.The Precise FormulaTo get the exact count of digits $L$ for any integer $n$, the formal math is:$$L = \lfloor \log_{10}(n) \rfloor + 1$$$\lfloor \dots \rfloor$ (Floor): This means "round down."$+ 1$: This accounts for the first digit.
Example: $n = 850$$\log_{10}(850) \approx 2.929$Round down (Floor) $\rightarrow 2$Add 1 $\rightarrow 3$$L = 3$ (Which is correct: 8, 5, 0).

Q 1056.https://leetcode.com/problems/confusing-number/
"""

class Solution:
    def confusingNumber(self, n: int) -> bool:
        #first invert
        inverted_map = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        #rotate
        rotated_number = []

        for char in str(n):
            if char not in inverted_map:
                return False
        
            #append the inverted digit of the number
            rotated_number.append(inverted_map[char])
        
        rotated_number = "".join(rotated_number)

        #slicing - start stop step size
        #start from end to begining 
        return int(rotated_number[::-1])!=n
        
