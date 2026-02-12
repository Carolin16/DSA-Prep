"""
       Q.225 https://leetcode.com/problems/implement-stack-using-queues/description/
        Time Complexity :
        push(x) O(n) Rotates the entire queue to put the new element at the front.
        pop()   O(1) Removes the element from the front of the deque.
        top()   O(1) Accesses the first element by index.
        empty() O(1) Checks if the internal deque has any elements.

        Space Complexity : O(1)
"""

from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        #enqueue at the tail of queue
        self.queue.append(x)

        #dequeue from the front and append at the end
        for _ in range(len(self.queue) - 1):
            element = self.queue.popleft()
            self.queue.append(element)

        

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return (not self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
