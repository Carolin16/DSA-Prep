"""
Q.155 https://leetcode.com/problems/min-stack/

Let n be the total number of operations performed.

Time Complexity : O(1) for all operations.

push(...): Checking the top of a Stack, comparing numbers, and pushing to the top of a Stack (or adding to the end of an Array or List) 
are all O(1) operations. Therefore, this overall is an O(1) operation.

pop(...): Popping from a Stack (or removing from the end of an Array, or List) is an O(1) operation.

top(...): Looking at the top of a Stack is an O(1) operation.

getMin(...): Same as above. This operation is O(1) because we do not need to compare values to find it. 
If we had not kept track of it on the Stack, and instead had to search for it each time, the overall time complexity would have been O(n).

Space Complexity : O(n).

Worst case is that all the operations are push. In this case, there will be O(2⋅n)=O(n) space used.
"""
class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:

        #Empty stack check
        #if self.stack is None - means it has to point to None object
        if not self.stack:
            self.stack.append((val , val))
            return 
        #self.stack[-1] returns the last element in the list or top of stack
        current_min = self.stack[-1][1]
        self.stack.append((val , min(current_min , val)))
        
    def pop(self) -> None:

        self.stack.pop()
        

    def top(self) -> int:
        
        return self.stack[-1][0]

    def getMin(self) -> int:
        
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
