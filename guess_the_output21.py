class Computers:
    def __init__(self, price):
        self.price = price
obj = Computers(30000)
obj.quantity = 12
obj.keyboard = 10
print(obj.quantity+len(obj.__dict__))
