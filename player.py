# Imports
import json
import type as itype
import uuid

# Global definitions
error_setting = bool()


class Player:
    """
    Holds all the data of a player and adds additional functionality
    with the Inventory instance.
    Creating a Player instance:

        Player = player.Player(username)

    [!] Check __docs__ for better visuals and explanations
    """

    def __init__(self, username, raise_errors: bool = True):
        # Initializes a new Player instance
        self.NAME = username  # Player's username
        self.HP = int()  # Health points
        self.XP = int()  # Experience points
        self.INVENTORY = _Inventory()  # Inventory Object
        self.WALLET = _Wallet()  # Amount of wealth/money
        self.HISTORY = list()  # History of Events

        # Setting for pushing or raising errors
        global error_setting
        error_setting = raise_errors


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

    def _getitem(self, uuid_: str):
        """
        Internal function.
        Returns the item object with the matching UUID.
        Raises a item not found warning upon failure.
        """
        for pos, ptr in enumerate(self.REGISTER):
            if ptr.UUID == uuid_:
                return ptr

        error('Item not found with ->', uuid_)

    def _getuuid(self, iid_: str):
        """
        Internal function.
        Returns the UUID of the first found object
        Raises a item not found warning upon failure.
        """
        for pos, ptr in enumerate(self.REGISTER):
            if ptr.ITEMID == iid_:
                return ptr.UUID

        error('Item not found with ->', iid_)

    def _getitempos(self, uuid_: str):
        """ Returns the position of the item in the register """
        for pos, ptr in enumerate(self.REGISTER):
            if ptr.UUID == uuid_:
                return pos

        error('Item not found with ->', uuid_)

    def __str__(self):
        """ Returns the list of ItemIDs in the register """
        names = (ptr.TYPE + '.' + ptr.ITEMID for ptr in self.REGISTER)
        return ', '.join(names)

    @property
    def register(self):
        """ Returns the list of object pointers """
        return self.REGISTER

    def get(self, iid_: str) -> object:
        """ Returns the first item with the selected ItemID """
        uuid_ = self._getuuid(iid_)
        return self._getitem(uuid_)

    def uget(self, uuid_: str) -> object:
        """ Returns the item instance by finding its unique UUID """
        return self._getitem(uuid_)

    def getdata(self, uuid_: str) -> dict:
        """
        Returns the dictionary containing all the data contained
        in the class instance. The first item in the dict is always
        the ItemID, then the UUID, and then the ItemType. Note that
        this is a one way operation, and the values within the item
        instance will not be changed when the dict is changed.
        """
        return self._getitem(uuid_).DATA

    def getuuid(self, iid_: str):
        """
        Returns the UUID of the first object found in the inventory
        with the matching ItemID
        """
        return self._getuuid(iid_)

    def getuuids(self, iid_: str):
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
        register. For this to not raise an error a valid ItemID
        needs to passed. Before creating an item it needs to be
        registered in src/ItemRegistry.json.
        """
        uuid_ = str(uuid.uuid4())

        try:
            # Fetching the item registry data
            with open('src/ItemRegistry.json') as f:
                iregister = json.loads(f.read())

                kwargs = iregister[iid]
                kwargs['amount'] = amount
                itemtype = kwargs['type']
                # Clearing the type from the data dict
                del kwargs['type']

            # Creating the object instance and appending it to the register
            setattr(self, iid, eval(f"itype.{itemtype}('{iid}', '{uuid_}', kwargs)"))
            exec(f"self.REGISTER.append(self.{iid})")

        except KeyError:
            error(f"'{iid}' has not been registered yet")


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
            error('Cannot remove more items then there is')

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
    def lastuuid(self) -> str:
        """ Returns the UUID of the newest item in the register """
        try:
            return self.REGISTER[-1].UUID
        except IndexError:
            return 'NONE'


class _Wallet:
    """
    The Wallet class adds complex interaction with the funds
    a player has.
    """
    def __init__(self):
        """ Creates a wallet """
        self.BALANCE = int()

    def add(self, amount):
        """ Add a certain amount of money to the wallet """
        self.BALANCE += amount

    def remove(self, amount):
        """ Remove money from the wallet """
        self.BALANCE -= amount

    def __str__(self) -> str:
        """ Returns the amount of money """
        return str(self.BALANCE)

    def __int__(self) -> int:
        """ Returns the amount of money as a int """
        return self.BALANCE

    @property
    def dollars(self) -> str:
        """ Returns a formatted version of the 'balance' """
        cents = self.BALANCE % 100
        dollars = (self.BALANCE - cents) / 100
        return '$' + str(int(dollars)) + '.' + str(cents)


class _History:
    """ Register for all the events that happened """
    def __init__(self):
        self.HISTORY = []

    def write(self, name, round_num):
        """ Appends a event to the history list """
        self.HISTORY.append({'event': name, 'round': round_num})

    @property
    def get(self) -> list:
        """ Returns the whole history """
        return self.HISTORY


class InventoryError(Exception):
    """ Custom error for the Inventory class """
    pass


def error(*msg):
    """
    Depending on the error_setting, it either prints a warning
    or raises a InventoryError exception
    """
    if error_setting:
        raise InventoryError(' '.join(msg))
    else:
        print('[!] InventoryError:', ' '.join(msg))


# voiding
type(itype)
