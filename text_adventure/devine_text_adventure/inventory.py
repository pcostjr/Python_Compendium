class Inventory:
    #creates a list of items
    #defaults to empty
    def __init__(self, items=[]):
        self.items = items

    #creates a list of items when printed
    def __str__(self):
        return "\n".join([item.name for item in self.items])

    #self.items wrapper method
    def get_items(self) -> list: return self.items

    #appends provided item to self.itens
    def add_item(self, item): self.items.append(item)

    #gets all items
    #converts them to just names
    #finds the index were the provided item name matches an itemname in the items list
    #returns item instance at the found index
    #if not IndexError should be expected
    def get_item(self, item_name):
        items = self.get_items()
        itemnames = [i.get_name() for i in items]
        idx = itemnames.index(item_name)
        return items[idx]

    #gets all items
    #converts them to just names
    #finds the index were the provided item name matches an itemname in the items list
    #removes item at index and returns it
    #if not IndexError should be expected
    def remove_item(self, item_name):
        items = self.get_items()
        itemnames = [i.get_name() for i in items]
        idx = itemnames.index(item_name)
        return self.items.pop(idx)
