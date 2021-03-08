class User:
    def __init__(self, name = "demo"):
        self.name=name

class Inventory:
    def __init__(self, slots = 0):
        self.slots = slots
        self.objects = dict()
    def add_object(self, obj):
        if obj in self.objects.keys():
            self.objects[obj] += 1
        else:
            self.objects[obj] = 1

        print(f"You have {self.objects[obj]} {obj}(s)")

def worthless_amount():
    return Price(price = {"cp":0,"sp":0,"ep":0,"gp":0,"pp":0})

class Price:
    def __init__(self, price):
        self.price = price

class Object:
    def __init__(self, name = "demo", bulk = 0, price = worthless_amount()):
        self.name = name
        self.bulk = bulk
        self.price = price
