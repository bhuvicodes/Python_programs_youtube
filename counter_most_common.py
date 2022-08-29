"""Code to find top 3
elements and
their counts
using most_common"""

from collections import Counter

arr = [1,2,4,3,2,3,1,4,3,1,2,3]
counter = Counter(arr)
top_three = counter.most_common(3)
print(top_three)
