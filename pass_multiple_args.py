def add_numbers(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(add_numbers(35,47,234,56,23,7))
