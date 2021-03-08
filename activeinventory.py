import price

class User:
    def __init__(self, name = "demo"):
        self.name=name

class Inventory:
    def __init__(self, slots = 0):
        self.slots = slots
        self.objects = dict()

class Object:
    def __init__(self, name = "demo", bulk = 0, price = price.zero()):
        self.name = name
        self.bulk = bulk
        self.price = price

