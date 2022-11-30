from abc import ABC, abstractmethod

class Goods(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def getPrice(self,cost):
        pass


class StationaryGood(Goods):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def getPrice(self):
        return self.price * self.quantity

class Magazine(Goods):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def getPrice(self):
        return self.price * self.quantity

class Book(Goods):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def getPrice(self):
        return (self.price * self.quantity) * 0.9

class Ribbon(Goods):
    def __init__(self, type, meters):
        self.type = type
        self.price = 5
        self.meters = meters
    
    def getPrice(self):
        return self.price * self.meters
    
def getTotalCost(basket):
    totalCost = 0
    for item in basket:
        totalCost += item.getPrice()
    return totalCost

basket = [Magazine("Computer World", 70, 3), Book("Windows 7 for Beginners", 200, 2), Ribbon("blue", 10)]
print(getTotalCost(basket))