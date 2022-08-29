val = ["823", "863"]
num = val[0][0:]
for row in range(0, len(val)):
    for column in range(0, len(val[row])):
        if num > val[row][column:]:
            num = val[row][column:]
print(num)