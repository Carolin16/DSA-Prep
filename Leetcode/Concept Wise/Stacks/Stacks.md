## 1. How are Stacks implemented in Python ?

1.Python does not have a built-in stack type, but stacks can be implemented in different ways using different data structures.

2.Using a List
  Python lists provide built-in methods that make them suitable for stack operations.
  The append () method adds an element to the end of the list.
  The pop () method removes and returns the last element from the list.

3.Using collections.deque
  Python’s collections module provides a deque (double-ended queue) for efficient insertions and deletions.
  The append () method adds an element to the right end of the deque.
  The pop () method removes and returns the element from the right end.
  Since deque is optimized for fast appends and pops, it is often preferred over lists for stack implementation.
