"""
Defines item types
"""


class Item:
    # Parent class for all items
    def __init__(self, name, value):
        self.NAME = name
        self.VALUE = value

    def __str__(self):
        return self.NAME

    def __repr__(self):
        return self.NAME + 'Item'


class Armor(Item):
    # Class for armour items
    def __init__(self, name, value, prot):
        super().__init__(name, value)
        self.PROTECTION = prot


class Weapon(Item):
    # Class for weapons
    def __init__(self, name, value, damage):
        super().__init__(name, value)
        self.DAMAGE = damage


class Food(Item):
    # Class for food items
    def __init__(self, name, value, cal):
        super().__init__(name, value)
        self.CALORIES = cal
