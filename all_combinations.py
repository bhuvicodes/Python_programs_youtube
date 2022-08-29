import itertools
val = [1,2,3,4,5]
total = len(list(itertools.permutations(val)))
print("The total number of combinations are", total)
for i in itertools.permutations(val):
    print("".join(str(j) for j in i), end = " | ")
    