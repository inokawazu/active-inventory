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

#Character
class Character(Inventory):
    def __init__(self, name = "demo", **kwargs):
        Inventory.__init__(self, kwargs)
        self.name=name

#Price
denomination_values = {"cp":1, "sp":10, "ep":50, "gp":100, "pp":1_000}

def parse_price_str(price_str):
    for denomination in denomination_values.keys():
        if denomination in price_str:
            return (int(price_str.replace(denomination, "")), denomination)
    else:
        return 0, "cp"

class Price:
    def __init__(self, price_str = "0"):
        price_str = price_str.strip()

        if price_str == "0":
            self.amount, self.denomination = 0, "cp"
        else:
            self.amount, self.denomination = parse_price_str(price_str)

    def __str__(self):
        return str(self.amount) + str(self.denomination)

    def __repr__(self):
        return f"Price(amount={self.amount},denomination={self.denomination})"

# Object
class Object:
    def __init__(self, name = "demo", bulk = 0, price = "0"):
        self.name = name
        self.bulk = bulk
        self.price = Price(price)

    def __hash__(self):
        return hash((self.name,self.bulk, str(self.price)))

    def __eq__(self, other):
        return (self.name,self.bulk, str(self.price)) == (other.name,other.bulk, str(other.price))

test_obj = Object(name = "test", bulk = 30, price="69sp")
test_inv = Inventory(slots = 100)


#############START BOT#############################################
import discord
from discord.ext import commands

description = '''
This bot keeps track of player inventories using the active-inventory system.
'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('---🤖---')

@bot.command()
async def start(ctx):
    #Checks if invoker is not in the current list of character
    #   If already there, the function send an error
    #Adds the invoker to the list.
    pass

# @client.event
# async def on_ready():
#     print('Active Inventory Bot ONLINE as {0.user} and ready '.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('>hello'):
#         await message.channel.send('Hello!')

#     if message.message.startswith('>h'):
#         await message.channel.send("I am a bot to help manage inventories of D&D characters!") #TODO Make a separate 'big string' for help.

#>start - makes character

#>inv
#>inventory - displays character inventory

#>give <item> [amount]

#>take <item> [amount]
