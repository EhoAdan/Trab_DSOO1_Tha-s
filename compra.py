from item import Item
from datetime import datetime

class Compra:

    def __init__(self, item: Item):
        self.__item = item
        self.__data = datetime.today().strftime("%m-%Y")
    
    @property
    def item(self):
        return self.__item
    
    @property
    def data(self):
        return self.__data
# Placeholder pro import compra não reclamar
