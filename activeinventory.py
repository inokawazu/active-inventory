class User:
    def __init__(self, name = "demo"):
        self.name=name

class Inventory:
    def __init__(self, slots = 0):
        self.slots = slots
        self.objects = dict()

    def add_object(self, obj, amount = 1):
        if obj in self.objects.keys():
            self.objects[obj] += amount
        else:
            self.objects[obj] = amount
        print(f"You have {self.objects[obj]} {obj}(s)")

    def remove_object(self, obj, amount = 1):
        if obj in self.objects.keys():
            if self.objects[obj] > amount:
                self.objects[obj] -= amount
                print(f"You have {self.objects[obj]} {obj}(s)")
            elif self.objects[obj] == amount:
                self.objects.pop(obj)
                print(f"You have no more {obj}s")
            else:
                print(f"You don't have at least {self.objects[obj]} {obj}(s)")
        else:
            print(f"You don't have any {obj} at all in the first place!")

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
