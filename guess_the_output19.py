count = 1
def doThis():
    global count
    for i in (1,2,3):
        count += 1
doThis()
print(count)
