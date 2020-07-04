"""
All of the players' data is stored in a instance of PlayerData.
"""
import type


class Player:
    def __init__(self, username):
        self.NAME = username
        self.HP = int()
        self.XP = int()
        self.INVENTORY = Inventory()  # Inventory Object
        self.HISTORY = list()  # History of Events


class Inventory:
    def __init__(self):
        self.LOCAL = {}

        # Item registry
        self.paper = type.Item('Paper', 10)
        self.apple = type.Food('Apple', 2, 120)
        self.basic_sword = type.Weapon('Basic Sword', 15, 5)
        self.basic_armor = type.Armor('Basic Armor', 15, 5)

    def add(self, name, amount):
        # Tries to add a new item to the item list, if fails creates a new item instance
        try:
            exec(f"self.LOCAL[self.{name}] += amount")
        except KeyError:
            exec(f"self.LOCAL[self.{name}] = amount")
        except AttributeError:
            print(f"'{name}' has not been registered yet")

        len([self.LOCAL, amount])  # void

    def remove(self, name, amount):
        # Removes the item from the name, does nothing if fails
        try:
            if amount == 'ALL':
                exec(f"del self.LOCAL[self.{name}]")
            else:
                exec(f"if self.LOCAL[self.{name}] < amount:"
                     f"\n\traise ItemError('Not enough items in inventory"
                     f" to remove')"
                     f"\nelse:\n\tself.LOCAL[self.{name}] -= amount")


        except KeyError:
            raise ItemError('This item does not exist in the inventory')

        len([self.LOCAL])  # void

    def clear(self):
        # Clear the whole inventory
        self.LOCAL = {}

    def __len__(self):
        # Returns the total amount of items
        local = int()
        for i in self.LOCAL:
            local += self.LOCAL[i]
        return local

    def __str__(self):
        out = []
        for i in self.LOCAL:
            if str(self.LOCAL[i]) != '1':
                out.append(str(i) + ' x' + str(self.LOCAL[i]))
            else:
                out.append(str(i))

        return '\n'.join(out)


class ItemError(Exception):
    pass
