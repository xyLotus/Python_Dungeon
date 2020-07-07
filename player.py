"""
All of the players' data is stored in a instance of PlayerData.
"""
import json
import type as itype
import uuid


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
        self.WALLET = _Wallet()  # Amount of wealth/money
        self.HISTORY = list()  # History of Events

    def save(self):
        """
        This functionality has been moved to the Serialization system
        """
        raise NotImplementedError('save() has been moved to serialization')

    def load(self):
        """
        This functionality has been moved to the Serialization system
        """
        raise NotImplementedError('load() has been moved to serialization')


class _Inventory:
    """
    Internal class only for the Player class, this should not
    be interacted with directly from the outside.
    """

    def __init__(self):
        """
        This is where the item register is created for use within
        the _Inventory class. There is only one item register for
        a player throughout the whole process.

        The register is a single-level list containing only pointers
        for the item instances created with the ItemTypes classes.
        The amount of items is stored inside the class instance.
        """
        self.REGISTER = []

    def _getitem(self, uuid_):
        """ Returns the item with the selected uuid """
        for pos, ptr in enumerate(self.REGISTER):
            if ptr.UUID == uuid_:
                return ptr

        raise InventoryError('Item not found')

    def _getuuid(self, iid_):
        """ Returns the uuid of the first item with the iid """
        for pos, ptr in enumerate(self.REGISTER):
            if ptr.ITEMID == iid_:
                return ptr.UUID

        raise InventoryError('Item not found')

    def _getitempos(self, uuid_):
        """ Returns the position of the item in the register """
        for pos, ptr in enumerate(self.REGISTER):
            if ptr.UUID == uuid_:
                return pos

        raise InventoryError('Item not found')

    def __str__(self):
        """ Returns the list of ItemIDs in the register """
        names = (ptr.TYPE + '.' + ptr.ITEMID for ptr in self.REGISTER)
        return ', '.join(names)

    @property
    def register(self):
        """ Returns the list of object pointers """
        return self.REGISTER

    def get(self, iid_) -> object:
        """ Returns the first item with the selected ItemID """
        uuid_ = self._getuuid(iid_)
        return self._getitem(uuid_)

    def uget(self, uuid_) -> object:
        """ Returns the item instance by finding its unique UUID """
        return self._getitem(uuid_)

    def getdata(self, uuid_) -> dict:
        """
        Returns the dictionary containing all the data contained
        in the class instance. The first item in the dict is always
        the ItemID, then the UUID, and then the ItemType. Note that
        this is a one way operation, and the values within the item
        instance will not be changed when the dict is changed.
        """
        return self._getitem(uuid_).DATA

    def getuuid(self, iid_):
        """
        Returns the UUID of the first object found in the inventory
        with the matching ItemID
        """
        return self._getuuid(iid_)

    def getuuids(self, iid_):
        """
        Returns the list of all UUIDs of the objects that match
        the given ItemID.
        """
        for i in self.REGISTER:
            if i.ITEMID == iid_:
                yield i.UUID

    def new(self, iid: str, amount: int = 1):
        """
        Creates a new item instance and adds the pointer to the
        register. For this to not raise an error, enough data
        needs to be passed. Import note: the data needs to be
        passed in a specific order to work for sure.

        > Player.INVENTORY.new('apple', 'Food', amount=12, ...)
        args -> ( ItemID, ItemType, **kwargs )

        If 3 or more normal arguments will be passed, it will
        raise an error.
        """
        uuid_ = str(uuid.uuid4())

        try:
            # Fetching the item registry data
            with open('src/ItemRegistry.json') as f:
                iregister = json.loads(f.read())

                kwargs = iregister[iid]
                kwargs['amount'] = amount
                itemtype = kwargs['type']

                del kwargs['type']

            # Creating the object instance and appending it to the register
            setattr(self, iid, eval(f"itype.{itemtype}('{iid}', '{uuid_}', kwargs)"))
            exec(f"self.REGISTER.append(self.{iid})")

        except KeyError:
            print(f"[!] '{iid}' has not been registered yet")


    def delete(self, uuid_):
        """ Removes a item """
        pos = self._getitempos(uuid_)
        del self.REGISTER[pos]

    def add(self, uuid_, amount):
        """ Adds a certain amount of items to the object """
        item = self._getitem(uuid_)
        item.AMOUNT += amount

    def remove(self, uuid_, amount):
        """ Removes a certain the amount of items from the object """
        item = self._getitem(uuid_)
        if item.AMOUNT >= amount:
            item.AMOUNT -= amount
        else:
            raise InventoryError('Cannot remove more items then there is')

    def clear(self):
        """ Clears the whole inventory, leaves a empty register """
        self.REGISTER = []

    @property
    def ids(self) -> list:
        """ Returns a list of item ids """
        ids = list(ptr.TYPE + '.' + ptr.ITEMID for ptr in self.REGISTER)
        return ids

    @property
    def uuids(self) -> list:
        """ Returns the uuids of the objects """
        uuids = list(ptr.UUID for ptr in self.REGISTER)
        return uuids

    @property
    def lastuuid(self):
        """ Returns the UUID of the newest item in the register """
        try:
            return self.REGISTER[-1].UUID
        except KeyError:
            return None


class _Wallet:
    """
    The Wallet class adds complex interaction with the funds
    a player has.
    """

    def __init__(self):
        """ Creates a wallet """
        self.MONEY = int()

    def add(self, amount):
        """ Add a certain amount of money to the wallet """
        self.MONEY += amount

    def remove(self, amount):
        """ Remove money from the wallet """
        self.MONEY -= amount

    def __str__(self):
        """ Returns the amount of money """
        return str(self.MONEY)

    @property
    def get(self):
        """ Returns the amount of money as a int """
        return self.MONEY

    @property
    def pretty(self):
        """ Returns a formatted version of the 'balance' """
        return None


class InventoryError(Exception):
    """
    This is raised when something goes wrong with the removal
    of items form the current inventory.
    """
    pass


# void
type(json)
type(itype)
