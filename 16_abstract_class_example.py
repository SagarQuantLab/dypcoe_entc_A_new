from abc import ABC, abstractmethod

class Govt(ABC):

    def __init__(self, name, age, aadhar):
        self.name = name
        self.age = age
        self.aadhar = aadhar

    @abstractmethod
    def get_license(self):
        pass
        
class pizzashop(Govt):

    def __init__(self, name, age, gender):
        Govt.__init__(self, name, age, gender)

    def get_license(self):
        return "I got my license"

pizzaShopIns = pizzashop('Rohan', 35, 1234567891011) 
print(pizzaShopIns.get_license())