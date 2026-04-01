# class my_class:
#     pass

class grandPa:

    def __init__(self, car, salary):
        self.car = car
        self.__salary = salary

    def _get_my_car(self):
        return f"You can drive my car {self.car} : from Grandpa"
    
    def __get_my_salary(self):
        return f"You can't access my salary : from Grandpa"
    
class papa(grandPa):

    def __init__(self, car, grandpa_salary, papa_salary):
        self.papa_salary = papa_salary
        grandPa.__init__(self, car, grandpa_salary)

    def get_papa_car(self):
        return self._get_my_car()
    
    def get_papa_salary(self):
        return self.__get_my_salary()
    
class childSon(papa):

    def __init__(self, car, grandpa_salary, papa_salary):
        papa.__init__(self, car, grandpa_salary, papa_salary)

    def get_grandpa_car(self):
        print(self._get_my_car())
        return self.get_papa_car()
    
    def get_papa_salary_new(self):
        return self.get_papa_salary()


# grandpaIns = grandPa('Swift', 50000)
# print(grandpaIns.car)
# # print(grandpaIns.__salary)
# print(grandpaIns._get_my_car())
# # print(grandpaIns.__get_my_salary())

# papaIns = papa('Swift', 50000, 80000)
# print(papaIns.get_papa_car())
# print(papaIns.get_papa_salary())

childSonIns = childSon('Swift', 50000, 80000)
print(childSonIns.get_grandpa_car())
print(childSonIns.get_papa_salary())