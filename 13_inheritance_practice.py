class Car:

    def __init__(self, maker_name, model, year):
        self.maker_name = maker_name
        self.model = model
        self.year = year

    def get_details(self):
        return f"My car details - {self.maker_name} - {self.model} - {self.year}"

class maruti(Car):

    def __init__(self, maker_name, model, year):
        Car.__init__(self, maker_name, model, year)


marutiIns = maruti("Maruti", "Swift", 2026)
print(marutiIns.get_details())


