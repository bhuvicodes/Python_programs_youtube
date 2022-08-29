# Python code to apply a function on a list

num = [10, 20, 30]

def double_num(result):
    return result * 2

new_num = list(map(double_num, num))
print(new_num)
