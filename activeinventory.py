# Inventory
class Inventory:

    def __init__(self, slots = 0):
        self.slots = slots
        self.objects = dict()

    def add_object(self, obj, amount = 1):
        if amount*obj.bulk + self.get_object_bulk() <= self.slots:
            if obj in self.objects.keys():
                self.objects[obj] += amount
            else:
                self.objects[obj] = amount
                print(f"You have {self.objects[obj]} {obj}(s)")
        else:
            print(f"You don't have enough room to fit {self.objects[obj]} {obj}(s)")

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

    def get_object_bulk(self):
        output_bulk = 0
        for obj, amount in self.objects.items():
            output_bulk += obj.bulk*amount
        return output_bulk

    def change_slots(self, slot_change):
        self.slots += slot_change
        print(f"You have {self.slots} now!")

class Character(Inventory):
    def __init__(self, name = "demo", **kwargs):
        Inventory.__init__(self, kwargs)
        self.name=name

def worthless_amount():
    return Price(price = {"cp":0,"sp":0,"ep":0,"gp":0,"pp":0})

def price_to_string(price_str):
    price = worthless_amount()
    for demonination in price.price.keys():
        if demonination in price_str:
            extracted_price = price_str.replace(demonination, "")
            price.price[demonination] = int(extracted_price)
            break
    return price

class Price:
    def __init__(self, price):
        self.price = price
        self._value = price["cp"]*1 + price["sp"]*10 + price["ep"]*50 + price["gp"]*100 + price["pp"]*1_000

    def __add__(self, other):
        plus_price_dict = {k:(self.price[k] + other.price[k]) for k in self.price.keys()}
        return Price(price = plus_price_dict)

    def __str__(self):
        price_str = ""

        for denomination, amount in self.price.items():
            if amount > 0:
                price_str += str(amount)
                price_str += denomination

        return price_str

class Object:
    def __init__(self, name = "demo", bulk = 0, price = worthless_amount()):
        self.name = name
        self.bulk = bulk
        self.price = price

    def __hash__(self):
        return hash((self.name,self.bulk, self.price._value))

    def __eq__(self, other):
        return (self.name,self.bulk, self.price._value) == (other.name,other.bulk, other.price._value)

test_obj = Object(name = "test", bulk = 30, price = Price({"cp":0,"sp":69,"ep":0,"gp":0,"pp":0}))
test_inv = Inventory(slots = 100)

#############START BOT#############################################
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Active Inventory Bot ONLINE as {0.user} and ready 🤖'.format(client))
