x = "abcdef"
i = "a"
while i in x:
    x = x[:-1]
    print(i, end = " ")