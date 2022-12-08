from abc import ABC, abstractmethod

class Sale_item:
	def __init__(self, name, cost, sale):
		self.name = name
		self.cost = cost
		self.sale = sale
		pass
	
	@abstractmethod
	def calculate_cost(self):
		pass

class Food(Sale_item):
	def __init__(self, name, cost, sale = 0):
		super().__init__(name, cost, sale)
		pass
	
	@abstractmethod
	def calculate_cost(self):
		pass

class Itemized_food(Food):
	def __init__(self, name, cost, amount):
		super().__init__(name, cost)
		self.amount = amount

	def calculate_cost(self):
		return self.cost * self.amount

class Measured_food(Food):
	def __init__(self, name, cost, weight):
		super().__init__(name, cost)
		self.weight = weight

	def calculate_cost(self):
		return self.cost * self.weight

class Book(Sale_item):
	def __init__(self, name, cost, sale, amount):
		super().__init__(name, cost, sale)
		self.amount = amount
	
	def calculate_cost(self):
		return self.cost * self.amount * (100 - self.sale) / 100

class Appliance(Sale_item):
	def __init__(self, name, cost, sale, amount):
		super().__init__(name, cost, sale)
		self.amount = amount
	
	def calculate_cost(self):
		return self.cost * self.amount * (100 + self.sale) / 100

vegtable = Itemized_food("Vegetable", 40, 2)
mango = Measured_food("Mango", 70, 1.8)
pythonbook = Book("Python", 200, 15, 1)
ricecooker = Appliance("Rice cooker", 1200, 7, 1)

poly = [vegtable, mango, pythonbook, ricecooker]

for i in poly:
    print(i.name, i.calculate_cost())