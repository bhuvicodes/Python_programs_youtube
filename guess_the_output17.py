s1 = {3, 4}
s2 = {1, 2}
s3 = set()
i = 0
j = 0
for i in s1:
    for j in s2:
        s3.add((i, j))
        i += 1
        j += 1
print(s3)
