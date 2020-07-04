"""
All of the players' data is stored in a instance of PlayerData.
"""
import type
import json


class Player:
    """
    Holds all the data of a player and adds additional functionality
    with the Inventory instance.
    Creating a Player instance:

        Player = player.Player(username)
    """

    def __init__(self, username):
        # Initialize a new Player instance
        self.NAME = username
        self.SYSNAME = username.replace(' ', '_')
        self.HP = int()
        self.XP = int()
        self.INVENTORY = _Inventory()  # Inventory Object
        self.HISTORY = list()  # History of Events

    def save(self):
        """
        Saves the current Player data in a json file found in
        /players/<username>.json

        Items in the inventory are stored with ItemIDs, not the
        instance pointers.
        """
        player_data = {'name': self.NAME,
                       'sysname': self.SYSNAME,
                       'hp': self.HP,
                       'xp': self.XP,
                       'inventory': self.INVENTORY.data,
                       'history': self.HISTORY}

        with open('players/' + self.SYSNAME + '.json', 'w') as f:
            data = json.dumps(player_data, indent=2)
            f.write(data)

    def load(self):
        """
        Loads the player data from /players/<username>.json
        and overwrites the current player data.
        Because items are saved as ItemIDs not as instance
        pointer, it cleans the inventory and adds the items
        to it, creating a Item instance from each ItemID
        """
        with open('players/' + self.SYSNAME + '.json') as f:
            data = json.loads(f.read())

        # Data loading
        self.NAME = data['name']
        self.SYSNAME = data['sysname']
        self.HP = data['hp']
        self.XP = data['xp']
        self.HISTORY = data['history']

        # Loads data into Inventory instance
        self.INVENTORY.clear()
        for item in data['inventory']:
            self.INVENTORY.add(item, data['inventory'][item])


class _Inventory:
    """
    Internal class only for the Player class, this should not
    be interacted with directly from the outside.
    """

    def __init__(self):
        """
        This is where items are registered calling the Item class
        and it's subclasses. Creating a new item is quite simple:

            self.<ItemID> = type.<ItemType>('<ItemID>', value, *)

        <ItemID> -> ItemIDs are lower_case_with_underscores
        <ItemType> -> Item types are registered in type.py/

        After registering the item here, it should be added to
        /lang/default.json. The key is the ItemID.
        If a default translation is not specified, it will
        fall back to the ItemID.
        """
        self.LOCAL = {}

        # Item registry
        self.coin = type.Item('coin', 1)
        self.gold_coin = type.Item('gold_coin', 100)
        self.paper = type.Item('paper', 10)
        self.apple = type.Food('apple', 2, 120)
        self.basic_sword = type.Weapon('basic_sword', 15, 5)
        self.basic_armor = type.Armor('basic_armor', 15, 5)

    def add(self, iid: str, amount: int):
        """
        Adds a item to the LOCAL item list using its ItemID.
        Supports adding items (current + additional).
        If the item was not registered in __init__,
        it will warn with > 'this' has not been registered yet <
        """
        try:
            exec(f"self.LOCAL[self.{iid}] += amount")
        except KeyError:
            exec(f"self.LOCAL[self.{iid}] = amount")
        except AttributeError:
            print(f"'{iid}' has not been registered yet")

        len([self.LOCAL, amount])  # voiding vars, don't mind it

    def add_list(self, array: list):
        """
        Adds a list of items to the LOCAL item list using add()
        Multiple items are supported, they just need to referenced
        more than once in the passed list.
        """
        for item in array:
            self.add(item, 1)

    def remove(self, iid: str, amount):
        """
        Remove a particular item from the list using its ItemID.
        You can either remove a amount of items or all of them using
        a int or 'ALL' in the amount argument.

        Removing more items than there is in the inventory will result
        in raising a ItemError. Same goes for nonexistent items.
        """
        try:
            if amount == 'ALL':
                exec(f"del self.LOCAL[self.{iid}]")
            else:
                exec(f"if self.LOCAL[self.{iid}] < amount:"
                     f"\n\traise ItemError('Not enough items in inventory"
                     f" to remove')"
                     f"\nelse:\n\tself.LOCAL[self.{iid}] -= amount")


        except KeyError:
            raise ItemError('This item does not exist in the inventory')

        len([self.LOCAL])  # voiding vars

    def clear(self):
        """ Clear the whole inventory, all the items. """
        self.LOCAL = {}

    def __len__(self) -> int:
        """
        Returns the total amount of items in the inventory,
        adds all the item amounts.
        """
        local = int()
        for i in self.LOCAL:
            local += self.LOCAL[i]
        return local

    def __str__(self) -> str:
        """
        Returns a pretty version of the Inventory dictionary, using
        already localized names and the amount. For developer friendly
        data use 'Player.INVENTORY.data' instead.
        """
        out = []
        for i in self.LOCAL:
            if str(self.LOCAL[i]) != '1':
                out.append(str(i) + ' x' + str(self.LOCAL[i]))
            else:
                out.append(str(i))

        return '\nYour Inventory:\n | ' + '\n | '.join(out) + '\n'

    @property
    def data(self) -> dict:
        """
        Returns the developer friendly dictionary of the current
        player inventory, with names as ItemIDs, not class pointers.
        """
        temp = {}
        for i in self.LOCAL:
            temp[repr(i)] = self.LOCAL[i]
        return temp


class ItemError(Exception):
    """
    This is raised when something goes wrong with the removal
    of items form the current inventory.
    """
    pass
