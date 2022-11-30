from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self, start, end, distance):
        pass
    
    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance
    
    def find_cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance
    
    def find_cost(self):
        return self.distance * 40

class Train(Transportation):
    def __init__(self, start, end, distance, station):
        self.start = start
        self.end = end
        self.distance = distance
        self.station = station
    
    def find_cost(self):
        return 5 * self.station

