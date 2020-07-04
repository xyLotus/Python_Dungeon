"""
Item types definitions
"""
import localization


class Item:
    """
    Parent class for all item types, super() this when
    creating a new ItemType. This parent class also handles
    the localization of the items.
    """

    def __init__(self, name, value):
        # Localization
        loc = localization.Localization()

        self.NAME = loc.translate('item', name)
        self.VALUE = value
        self.ITEMID = name

    def __str__(self) -> str:
        """ Returns the localized item name """
        return self.NAME

    def __repr__(self) -> str:
        """
        Returns the ItemID with a 'item:' prefix for use
        in Player.INVENTORY.data
        """
        return 'item:' + self.ITEMID

    @property
    def id(self) -> str:
        """ Returns the ItemID """
        return self.ITEMID


class Armor(Item):
    """ Additional: protection """
    def __init__(self, name, value, prot: int):
        super().__init__(name, value)
        self.PROTECTION = prot


class Weapon(Item):
    """ Additional: damage """
    def __init__(self, name, value, damage: int):
        super().__init__(name, value)
        self.DAMAGE = damage


class Food(Item):
    """ Additional: calories """
    def __init__(self, name, value, cal: int):
        super().__init__(name, value)
        self.CALORIES = cal
