class Item:
    #creates an item with a name
    def __init__(self, name):
        self.name = name

    #self.name wrapper method
    def get_name(self): return self.name
