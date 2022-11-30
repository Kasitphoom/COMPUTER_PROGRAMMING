class Name:
    def __init__(self, title, first, last):
        self.title = title
        self.first = first
        self.last = last
        
    def setName(self, title, first, last):
        self.title = title
        self.first = first
        self.last = last
    
    def getFullName(self):
        return f"full name = {self.title}. {self.first} {self.last}"

class Date:
    def __init__(self, day, month, year):
        if day > 31:
            month += day // 31
            day %= 31
        if month > 12:
            year += month // 12
            month %= 12
            
        self.day = day
        self.month = month
        self.year = year
    
    def setDate(self, day, month, year):
        if day > 31:
            month += day // 31
            day %= 31
        if month > 12:
            year += month // 12
            month %= 12
            
        self.day = day
        self.month = month
        self.year = year
    
    def getDate(self):
        return f"date = {self.day}/{self.month}/{self.year}"
    
    def getDateBC(self):
        return f"date = {self.day}/{self.month}/{self.year + 543} BC"
    
class Address:
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode
    
    def setAddress(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode
        
    def getAddress(self):
        return f"address = {self.houseNo} {self.street} {self.district} {self.city} {self.country} {self.postcode}"

class Department:
    def __init__(self, description, manager, employeeList):
        self.description = description
        self.manager = manager
        self.employeeList = employeeList
    
    def addEmployee(self, employee):
        self.employeeList.append(employee)
        employee.department = self
    
    def deleteEmployee(self, employee):
        self.employeeList.remove(employee)
        employee.department = None
        
    
    def setManager(self, manager):
        if manager in self.employeeList:
            self.manager = manager
        else:
            print("Manager is not in employee list")
            return
    
    def printInfo(self):
        print(f"Department: {self.description}")
        print(f"Manager: {self.manager.getFullName()}")
        print(f"Employee List:")
        for employee in self.employeeList:
            print(employee.getFullName())
            
class Person:
    def __init__(self, name, dateOfBirth, address):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address
        
    def printInfo(self):
        print(f"Name: {self.name.getFullName()} {self.dateOfBirth} {self.address}")
        
class Employee(Person):
    def __init__(self, name, dateOfBirth, address, startdate, department):
        super().__init__(name, dateOfBirth, address)
        self.startdate = startdate
        self.department = department
        
    def printInfo(self):
        return super().printInfo() + f" {self.startdate} {self.department.printInfo()}"
    
class TempEmployee(Employee):
    def __init__(self, name, dateOfBirth, address, startdate, department, wage):
        super().__init__(name, dateOfBirth, address, startdate, department)
        self.wage = wage
        
    def printInfo(self):
        return super().printInfo() + f" {self.wage}"
    
class PermEmployee(Employee):
    def __init__(self, name, dateOfBirth, address, startdate, department, salary):
        super().__init__(name, dateOfBirth, address, startdate, department)
        self.salary = salary
        
    def printInfo(self):
        return super().printInfo() + f" {self.salary}"