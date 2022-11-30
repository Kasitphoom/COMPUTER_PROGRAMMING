class Earth():
    def __init__(self, name = "Earth", age = 18):
        self.name = name
        self.age = age
        
    def Name(self):
        return self.name
    
    def Age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name
        
e = Earth("EEEEEE", 16)
e2 = Earth()

print(e.name)
print(e2.name)