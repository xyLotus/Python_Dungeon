# Python_Dungeon
A basic Python command line RPG.
This Project was made with some of the pre-installed modules by the python default settings.
We created this project out of boredom and fun, I hope you enjoy it!

- Lead Developer: xyLotus
- Background Developer: bellrise


### Player instance interaction

Create a new Player:
````python
self.Player = player.Player(username)
````




##### Player Inventory interaction

Adding items 
```python
self.Player.INVENTORY.add('<ItemID>', amount)
```

Removing items
````python
self.Player.INVENTORY.remove('<ItemID>', amount)
````

Adding a list of items
````python
self.Player.INVENTORY.add_list(<ItemIDList>)
````

Clearing the inventory
````python
self.Player.INVENTORY.clear()
````

Printing the inventory
````python
print(self.Player.INVENTORY)
```` 
