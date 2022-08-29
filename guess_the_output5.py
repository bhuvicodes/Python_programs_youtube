dictionary = {}
dictionary[1] = 1
dictionary["1"] = 2
dictionary[1] += 1

sum = 0
for k in dictionary:
    sum += dictionary[k]
print(sum)
