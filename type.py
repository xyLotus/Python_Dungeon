"""
Item types definition
"""
import localization


class Item:
    """
    Parent class for all item types, super() this when
    creating a new ItemType. This parent class also handles
    the localization of the items.
    """
    def __init__(self, iid, uuid):
        # Localization
        loc = localization.Localization()
        self.NAME = loc.translate('item', iid)

        self.UUID = uuid
        self.ITEMID = iid
        self.TYPE = self.__class__.__name__
        self.DATA = {'iid': self.ITEMID,
                     'uuid': self.UUID,
                     'type': self.TYPE,
                     'name': self.NAME}

    def __str__(self) -> str:
        """ Returns the human-readable object pointer """
        return self.TYPE + '.' + self.ITEMID


class Stackable(Item):
    """ Class for stackable items """
    def __init__(self, iid, uuid, v: dict):
        super().__init__(iid, uuid)
        self.AMOUNT = v['amount']
        self.DATA['amount'] = self.AMOUNT


# ItemType Classes

class Armor(Item):
    """ Additional: protection """
    def __init__(self, iid, uuid, v: dict):
        super().__init__(iid, uuid)
        self.PROTECTION = v['prot']
        self.DATA['prot'] = self.PROTECTION


class Weapon(Item):
    """ Additional: damage """
    def __init__(self, iid, uuid, v: dict):
        super().__init__(iid, uuid)
        self.DAMAGE = v['damage']
        self.DATA['damage'] = self.DAMAGE


class Food(Stackable):
    """ Additional: calories """
    def __init__(self, iid, uuid, v: dict):
        super().__init__(iid, uuid, v)
        self.CALORIES = v['cal']
        self.DATA['cal'] = self.CALORIES
