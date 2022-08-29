def func(a, b):
    if a - b:
        return a + b
    else:
        return a * b

def func2():
    ans = 0
    i = 1
    while(i*i <= 20):
        ans += func(i, i)
        i += 1
    print(ans)
func2()
