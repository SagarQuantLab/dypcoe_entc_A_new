from abc import ABC, abstractmethod

class College(ABC):

    def __init__(self, name, age, gender, section):
        self.name = name
        self.age = age
        self.gender = gender
        self.section = section

    @abstractmethod
    def enrollement(self):
        pass

class Student(College):

    def __init__(self, name, age, gender, section):
        College.__init__(self, name, age, gender, section)

    def enrollement_updated(self):
        return "Abstract method implemented"
    
    def enrollement(self):
        return "My enrollment is done"
        
    
sIns = Student("Rohan", 20, "M", "ENTC - A")
print(sIns.enrollement_updated())
print(sIns.enrollement())