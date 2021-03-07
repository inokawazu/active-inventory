# Entity
class Entity:
    def __init__(self, name = "unknown",
                 location = "nowhere",
                 condition = "fine",
                 size = "Medium"):
        self._name = name
        self._location = location
        self._condition = condition
        self._size = size

    def get_name(self):
        return self._name
    def get_location(self):
        return self._location
    def get_condition(self):
        return self._condition
    def get_size(self):
        return self.get_size

    def set_name(self, name):
        print(f"Name was changed from {self._name} to {name}.")
        self._name = name
    def set_location(self, location):
        print(f"Location was moved from {self._location} to {location}.")
        self._location = location
    def set_condition(self, condition):
        print(f"Condition was changed from {self._condition} to {condition}.")
        self._condition = condition
    def set_size(self, size):
        print(f"Size was changed from {self._size} to {size}.")
        self._size = size

class Inventory():
    def __init__(self,slots = 0, objects = dict()):
        self._slots = slots
        self._objects = objects

    def get_slots(self):
        return self._slots
    def get_objects(self):
        return self._objects

    def add_object(self, object, count = 1):
        pass
    def remove_object(self, object, count = 1):
        pass

class Attributes:
    default_attributes = {"Str":10,
                          "Con":10,
                          "Dex":10,
                          "Int":10,
                          "Wis":10,
                          "Cha":10}
    def __init__(self, attributes = Attributes.default_attributes):
        self._attributes = attributes

class Creature(Entity, Attributes):
    creature_bulk_dict = {"Tiny":5,
                          "Small":10,
                          "Medium":20,
                          "Large":40,
                          "Huge":80,
                          "Gargantuan":160}
    def __init__(self, **kwargs):
        Entity.__init__(self,kwargs)
        Attributes.__init__(self, kwargs)
        self._bulk = self.creature_bulk_dict[self._size]
