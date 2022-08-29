numbers = [30, 42, 28, 50, 15]
for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
       numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
       numbers[i] = 'fizz'
    elif num % 5 == 0:
       numbers[i] = 'buzz'
print(numbers) # ['fizzbuzz', 'fizz', 28, 'buzz', 'fizzbuzz']