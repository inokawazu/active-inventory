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
                return f"You have {self.objects[obj]} {obj}(s)"
        else:
            return f"You don't have enough room to fit {self.objects[obj]} {obj}(s)"

    def remove_object(self, obj, amount = 1):
        if obj in self.objects.keys():
            if self.objects[obj] > amount:
                self.objects[obj] -= amount
                return f"You have {self.objects[obj]} {obj}(s)"
            elif self.objects[obj] == amount:
                self.objects.pop(obj)
                return f"You have no more {obj}s"
            else:
                return f"You don't have at least {self.objects[obj]} {obj}(s)"
        else:
            return f"You don't have any {obj} at all in the first place!"

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

    def __str__(self):
        return self.name

test_obj = Object(name = "test", bulk = 30, price="69sp")
test_inv = Inventory(slots = 100)

#############START BOT#############################################
import discord
from discord.ext import commands

description = '''
This bot keeps track of player inventories using the active-inventory system.
'''

users = []

def add_user(username, slots):
    global users
    users.append(Character(name = username, slots = slots))

def is_added_user(username):
    global users
    for user in users:
        if username == user.name:
            return True
    else:
        return False

def change_user_slots(username, new_slots):
    global users
    for user in users:
        if username == user.name:
            user.slots = new_slots
            return "Success"
    return "Not Found"

def give_user_object(username, obj:Object, amount):
    global users
    for user in users:
        if username == user.name:
            return user.add_object(obj, amount)
    else:
        return f"{username} was not found."

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('---🤖---')

@bot.event
async def on_command(ctx):
    print(f"{ctx.author} has used {ctx.command} in {ctx.channel}")

@bot.command()
async def newslots(ctx,new_amount):
    try:
        new_amount_int = int(new_amount)
        if not is_added_user(ctx.author):
            add_user(ctx.author, new_amount_int)
        else:
            change_user_slots(ctx.author, new_amount_int)
        await ctx.send(f"{ctx.author} now has {new_amount_int} slots.")
    except Exception as e:
        await ctx.send(e)
        await ctx.send(f"You need to write the command as {bot.command_prefix}newslots <new amount of slots>")

@bot.command()
async def add(ctx, item_amount, item_name, slots_per_item, worth_per_item):
    try:
        item_amount_int = int(item_amount)
        slots_per_item_int = int(slots_per_item)
        if not is_added_user(ctx.author):
            await ctx.send(f"Please use the {bot.command_prefix}newslots first.")
        else:
            obj_to_give = Object(name=item_name, bulk=slots_per_item_int,price=worth_per_item)
            await ctx.send(give_user_object(ctx.author, obj_to_give, item_amount_int))
    except:
        await ctx.send(f"You need to write the command as {bot.command_prefix}<new amount of slots>")
