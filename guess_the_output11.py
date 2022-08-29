count = 1

def func():
    global count

    for i in (1,2,3):
        count += 1

func()
print(count)
