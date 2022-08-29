"""Python code to find
2 largest and 2 smallest
elements of a list."""

import heapq

marks = [100, 80, 30, 60, 90]
print(heapq.nsmallest(2, marks))
print(heapq.nlargest(2, marks))
