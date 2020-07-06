# Instructions for using the tools

### Player instance creation

Creating a new player:
````python
self.Player = player.Player(username)
````
___
### Player inventory interaction

The `INVENTORY` attribute of the `Player` instance is actually a hidden class with several methods
and attributes. For complex interaction items are actually instances of a ItemType class (`type.py`).
That way a item can have multiple attributes and methods for operating on itself. The item instances are held
in the inventory register. Accessing data within the `Inventory` class can be done with its methods.
```python
# Getting the list of items (the pointers)
x = self.Player.INVENTORY.register
```
Printing the register will result in a list of unreadable instance pointers

Example: 
> `[<type.Food object at 0x02E5E838>, <type.Weapon object at 0x02E5E868>]`

For better readability, printing the `INVENTORY` itself will yield a string of ItemIDs with their types:
> `Food.apple, Weapon.sword`

___
#### Getting the UUID of an item
There is two ways of doing this, either using `getuuid()` or accesing the items in the registry.
The first way is only if you have a single item with the ItemID.
```python
# First way
uuid = self.Player.INVENTORY.getuuid(<ItemID>)
# Note: This way gets ONLY THE FIRST item with the matching ItemID

# Second way (will return a list of them)
uuids = list(self.Player.INVENTORY.getuuids(<ItemID>)
```
___
#### Getting a item object
To modify a item you need to operate on the item object itself.
First, you need to get that item using it's _ItemID_ or _UUID_.
Using a _ItemID_ is easier, but works as long as you have one instance of that item.
With a _UUID_ you can choose the particular item, even if there are multiple with the same _ItemID_.
```python
# Using the ItemID
item = self.Player.INVENTORY.get(<ItemID>)

# Using a UUID
item = self.Player.INVENTORY.uget(<UUID>)
```
___
#### Creating and modifying items
After getting the item, operations can be done on the item object directly changing its values,
or using Inventory methods to do so.

Using Inventory methods:
```python
# Creating a new item
self.Player.INVENTORY.new(<ItemID>, <ItemType>, amount=<amount>, ...) 

# Deleting a item
self.Player.INVENTORY.delete(<UUID>)

# Increasing the amount of an item
self.Player.INVENTORY.add(<UUID>, <amount>)

# Decreasing the amount of an item
self.Player.INVENTORY.remove(<UUID>, <amount>)

# Clearing the inventory
self.Player.INVENTORY.clear()
```

Directly changing the values of the item object:

This is much more versitile, you can change every value operating on the object. 

Note: `item` is the previously created item object with `get()` or `uget()`.
```python
# Changing the amount (this works only for ItemTypes which inherited from Stackable!)
item.AMOUNT = <value>

# You can do this with every item attribute
item.<attribute> = <value>


# Printing the inventory
print(self.Player.INVENTORY)
```
___
#### Other inventory methods
```python
# Getting the list of ItemIDs
x = self.Player.INVENTORY.ids

# Getting the list of UUIDs
x = self.Player.INVENTORY.uuids
```

### Player wallet interaction
The `WALLET` attribute is separated from the `INVENTORY` attribute, so it has it's own set of methods.
```python
# Adding/removing money from the wallet 
self.Player.WALLET.add(<amount>)
self.Player.WALLET.remove(<amount>)

# Getting the balance
balance = self.Player.WALLET.get
```

## Object Serialization
Saving objects, or serializing them is done with the `Pack` class in `serialization.py`.
Serializing them is quite straightforward, the only thing you need is the path and the object itself.
Example with the Player instance:
```python
from serialization import Pack

...

# Packing
Pack.save(<object>, <path>)

# Unpacking
obj = Pack.load(<path: str>)
```
The packing and unpacking is handled by `pickle`, so loading the packed file will return a class instance, with all the methods and attributes.
Note: Every kind of data can be saved, not only class instances.

## Data values
```
Examples

<ItemID>    = 'this_is_a_item_id'                     # lowercase with underscores
<UUID>      = '9c385152-e8a4-4d69-8eb3-439158a799e2'  # auto-generated str
<amount>    = 12                                      # int
<value>     = 3 | 'something'                         # can be a string or a int
<path>      = 'file/players/test.txt'                 # only forward-slashes
<attribute> = EXAMPLEATTRIBUTE                        # all caps no spaces
<object>    = <type.Food object at 0x02E5E838>        # class instance
```

## What not to do:
- Do not `import main` **anywhere** because it will most likely result in a `RecursionError` 
